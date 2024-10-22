"""
The below represents a node and a singly-linked list in code
"""

from typing import Any, Optional


class Node:
    # Initializer AKA constructor
    def __init__(self, value: Any):
        self.value = value
        self.next = None


class SinglyLinkedList:
    # Initializer AKA constructor
    def __init__(self, value: Any):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # Returns a node at a specified index of the SinglyLinkedList object
    def get(self, index: int) -> Optional[Node]:
        # Checks if index is out of range
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        # Usually an i would be used as the variable in a for loop however, if it's not going to be used, in general
        # it's good practice to use an _ underscore instead when ANY variable is not going to be used in code since
        # you're only supposed to use a variable in code if it's actually going to be used
        for _ in range(index):
            temp = temp.next
        return temp

    # Sets/updates the value of a node at a specified index of the SinglyLinkedList object
    def set_value(self, index: int, value: Any):
        temp = self.get(index)
        if temp:
            temp.value = value

    # Adds a new node to the end of the SinglyLinkedList object
    def append(self, value: Any) -> bool:
        new_node = Node(value)
        # Checks if the SinglyLinkedList is empty
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        # Otherwise, adds the new node to the end of the SinglyLinkedList
        else:
            # Points the next link of the tail node to the new node
            self.tail.next = new_node
            # Points the tail node to the new node which is now the last node at the end of the SinglyLinkedList
            self.tail = new_node
        self.length += 1
        return True

    # Adds a new node to the front of the SinglyLinkedList object
    def prepend(self, value: Any) -> bool:
        new_node = Node(value)
        # Checks if the SinglyLinkedList is empty
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        # Otherwise, adds the new node to the front of the SinglyLinkedList
        else:
            # Points the next link of the new node to the first node
            new_node.next = self.head
            # Points the head node to the new node which is now the first node at the front of the SinglyLinkedList
            self.head = new_node
        self.length += 1
        return True

    # Removes the last node at the end of the SinglyLinkedList object
    def pop(self) -> Optional[Node]:
        # Checks if the SinglyLinkedList is empty
        if self.length == 0:
            return None
        # Otherwise, removes the last node at the end of the SinglyLinkedList
        # Remember that an else conditional should not be used and is unnecessary if a previous return statement is used
        # since it will default to the next return statement once the first return statement doesn't execute
        temp = self.head
        prev = self.head
        while temp.next:
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = None
        self.length -= 1
        # Accounts for when there is only 1 node in the SinglyLinkedList
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    # Removes the first node at the front of the SinglyLinkedList object
    def pop_first(self) -> Optional[Node]:
        # Checks if the SinglyLinkedList is empty
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        # Accounts for when there is only 1 node in the SinglyLinkedList
        if self.length == 0:
            self.tail = None
        return temp

    # Inserts a new node to a specified index of the SinglyLinkedList object
    def insert(self, index: int, value: Any) -> bool:
        # Checks if index is out of range
        if index < 0 or index > self.length:
            return False
        # Inserts the new node to the front of the SinglyLinkedList
        if index == 0:
            return self.prepend(value)
        # Inserts the new node to the end of the SinglyLinkedList
        if index == self.length:
            return self.append(value)
        # Inserts the new node to the specified index (somewhere in the middle) of the SinglyLinkedList
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    # Removes a node at a specified index of the SinglyLinkedList object
    def remove(self, index: int) -> Optional[Node]:
        # Checks if index is out of range
        if index < 0 or index >= self.length:
            return None
        # Alternative code however it is O(n)
        # temp = self.get(index)
        # Removes the first node at the front of the SinglyLinkedList
        if index == 0:
            return self.pop_first()
        # Removes the last node at the end of the SinglyLinkedList
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        # Removes the node at the specified index (somewhere in the middle) of the SinglyLinkedList
        # More efficient code since it is O(1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    # Reverses the order of the SinglyLinkedList object
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before_node = None
        for _ in range(self.length):
            after_node = temp.next
            temp.next = before_node
            before_node = temp
            temp = after_node

    # Prints the value of each node of the SinglyLinkedList object
    def display_linked_list(self):
        if self.head is None:
            print("Empty linked list")
        else:
            values = []
            current_node = self.head
            while current_node:
                values.append(str(current_node.value))
                current_node = current_node.next
            values.append("None")
            print(" -> ".join(values))

        # The code below has been refactored to the code above
        # current_node = self.head
        # while current_node:
        #     print(current_node.value)
        #     current_node = current_node.next

    # Makes the SinglyLinkedList object empty
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0


if __name__ == "__main__":
    print("\n----- Test: Instantiates a SinglyLinkedList -----\n")
    my_singly_linked_list = SinglyLinkedList(4)
    print("head node value:", my_singly_linked_list.head.value)
    print("head node next link:", my_singly_linked_list.head.next)
    print("")

    print("linked list:")
    my_singly_linked_list.display_linked_list()
    print("linked list length:", my_singly_linked_list.length)

    print("\n----- Test: Appends a node to the SinglyLinkedList -----\n")
    my_singly_linked_list.append(5)
    print("head node value:", my_singly_linked_list.head.value)
    print("head node next link:", my_singly_linked_list.head.next)
    print("next node value:", my_singly_linked_list.head.next.value)
    print("next node next link:", my_singly_linked_list.head.next.next)
    print("tail node value:", my_singly_linked_list.tail.value)
    print("tail node next link:", my_singly_linked_list.tail.next)
    print("")

    print("linked list:")
    my_singly_linked_list.display_linked_list()
    print("linked list length:", my_singly_linked_list.length)

    print("\n----- Test: .pop() on SinglyLinkedList with multiple nodes -----\n")
    print("linked list:")
    my_singly_linked_list.display_linked_list()
    print("linked list length:", my_singly_linked_list.length)
    print("")

    print("popped node:", my_singly_linked_list.pop().value)
    print("linked list:")
    my_singly_linked_list.display_linked_list()
    print("linked list length:", my_singly_linked_list.length)

    print("\n----- Test: .pop() on SinglyLinkedList with one node -----\n")
    print("linked list:")
    my_singly_linked_list.display_linked_list()
    print("linked list length:", my_singly_linked_list.length)
    print("")

    print("popped node:", my_singly_linked_list.pop().value)
    print("linked list:")
    my_singly_linked_list.display_linked_list()
    print("linked list length:", my_singly_linked_list.length)

    print("\n----- Test: .pop() on an empty SinglyLinkedList -----\n")
    print("linked list:")
    my_singly_linked_list.display_linked_list()
    print("linked list length:", my_singly_linked_list.length)
    print("")

    print("popped node:", my_singly_linked_list.pop())
    print("linked list:")
    my_singly_linked_list.display_linked_list()
    print("linked list length:", my_singly_linked_list.length)

    print("\n----- Test: Prepends a node to an empty SinglyLinkedList -----\n")
    my_singly_linked_list.prepend(3)
    print("linked list:")
    my_singly_linked_list.display_linked_list()
    print("linked list length:", my_singly_linked_list.length)

    print("\n----- Test: Prepends multiple nodes to the SinglyLinkedList -----\n")
    my_singly_linked_list.prepend(2)
    my_singly_linked_list.prepend(1)
    print("linked list:")
    my_singly_linked_list.display_linked_list()
    print("linked list length:", my_singly_linked_list.length)

    print("\n----- Test: .pop_first() on SinglyLinkedList with multiple nodes -----\n")
    print("linked list:")
    my_singly_linked_list.display_linked_list()
    print("linked list length:", my_singly_linked_list.length)
    print("")

    print("popped node:", my_singly_linked_list.pop_first().value)
    print("linked list:")
    my_singly_linked_list.display_linked_list()
    print("linked list length:", my_singly_linked_list.length)
    print("")

    print("popped node:", my_singly_linked_list.pop_first().value)
    print("linked list:")
    my_singly_linked_list.display_linked_list()
    print("linked list length:", my_singly_linked_list.length)

    print("\n----- Test: .pop_first() on SinglyLinkedList with one node -----\n")
    print("linked list:")
    my_singly_linked_list.display_linked_list()
    print("linked list length:", my_singly_linked_list.length)
    print("")

    print("popped node:", my_singly_linked_list.pop_first().value)
    print("linked list:")
    my_singly_linked_list.display_linked_list()
    print("linked list length:", my_singly_linked_list.length)

    print("\n----- Test: .pop_first() on an empty SinglyLinkedList -----\n")
    print("linked list:")
    my_singly_linked_list.display_linked_list()
    print("linked list length:", my_singly_linked_list.length)
    print("")

    print("popped node:", my_singly_linked_list.pop_first())
    print("linked list:")
    my_singly_linked_list.display_linked_list()
    print("linked list length:", my_singly_linked_list.length)

    print("\n----- Test: .get() on SinglyLinkedList with multiple nodes -----\n")
    my_singly_linked_list.append(0)
    my_singly_linked_list.append(1)
    my_singly_linked_list.append(2)
    my_singly_linked_list.append(3)
    print("linked list:")
    my_singly_linked_list.display_linked_list()
    print("linked list length:", my_singly_linked_list.length)
    print("")

    print("node value at index 2:", my_singly_linked_list.get(2).value)
    print("node value at index -1:", my_singly_linked_list.get(-1))
    print("node value at index 4:", my_singly_linked_list.get(4))
    print("node value at index 10:", my_singly_linked_list.get(10))

    print("\n----- Test: .set_value() on SinglyLinkedList with multiple nodes -----\n")
    my_singly_linked_list.make_empty()
    my_singly_linked_list.append(1)
    my_singly_linked_list.append(2)
    my_singly_linked_list.append(5)
    my_singly_linked_list.append(4)
    print("linked list:")
    my_singly_linked_list.display_linked_list()
    print("linked list length:", my_singly_linked_list.length)
    print("")

    my_singly_linked_list.set_value(2, 3)
    print("linked list:")
    my_singly_linked_list.display_linked_list()
    print("linked list length:", my_singly_linked_list.length)

    print("\n----- Test: .insert() on SinglyLinkedList with multiple nodes -----\n")
    my_singly_linked_list.make_empty()
    my_singly_linked_list.append(1)
    my_singly_linked_list.append(3)
    print("linked list:")
    my_singly_linked_list.display_linked_list()
    print("linked list length:", my_singly_linked_list.length)
    print("")

    my_singly_linked_list.insert(1, 2)
    print("linked list:")
    my_singly_linked_list.display_linked_list()
    print("linked list length:", my_singly_linked_list.length)
    print("")

    my_singly_linked_list.insert(0, 0)
    print("linked list:")
    my_singly_linked_list.display_linked_list()
    print("linked list length:", my_singly_linked_list.length)
    print("")

    my_singly_linked_list.insert(4, 4)
    print("linked list:")
    my_singly_linked_list.display_linked_list()
    print("linked list length:", my_singly_linked_list.length)

    print("\n----- Test: .remove() on SinglyLinkedList with multiple nodes -----\n")
    my_singly_linked_list.make_empty()
    my_singly_linked_list.append(15)
    my_singly_linked_list.append(1)
    my_singly_linked_list.append(2)
    my_singly_linked_list.append(10)
    my_singly_linked_list.append(3)
    my_singly_linked_list.append(4)
    my_singly_linked_list.append(27)
    print("linked list:")
    my_singly_linked_list.display_linked_list()
    print("linked list length:", my_singly_linked_list.length)
    print("")

    print("removed node at index 3:", my_singly_linked_list.remove(3).value)
    print("linked list:")
    my_singly_linked_list.display_linked_list()
    print("linked list length:", my_singly_linked_list.length)
    print("")

    print("removed node at index 0:", my_singly_linked_list.remove(0).value)
    print("linked list:")
    my_singly_linked_list.display_linked_list()
    print("linked list length:", my_singly_linked_list.length)
    print("")

    print("removed node at index 4:", my_singly_linked_list.remove(4).value)
    print("linked list:")
    my_singly_linked_list.display_linked_list()
    print("linked list length:", my_singly_linked_list.length)

    print("\n----- Test: .reverse on SinglyLinkedList with multiple nodes -----\n")
    my_singly_linked_list.make_empty()
    my_singly_linked_list.append(1)
    my_singly_linked_list.append(2)
    my_singly_linked_list.append(3)
    my_singly_linked_list.append(4)
    print("linked list:")
    my_singly_linked_list.display_linked_list()
    print("linked list length:", my_singly_linked_list.length)
    print("")

    my_singly_linked_list.reverse()
    print("linked list:")
    my_singly_linked_list.display_linked_list()
    print("linked list length:", my_singly_linked_list.length)
