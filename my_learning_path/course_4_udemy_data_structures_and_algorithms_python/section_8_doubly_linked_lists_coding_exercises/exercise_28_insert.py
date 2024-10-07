"""
Implement the insert method for the DoublyLinkedList class that inserts a new node with a given value at a specific
index in the linked list
- The method should perform the following tasks:
    1. If the given index is out of bounds (i.e., it is less than 0 or greater than the linked list length), return
    False
    2. If the index is 0, call the prepend method with the provided value and return its result
    3. If the index is equal to the linked list length, call the append method with the provided value and return its
    result
    4. Create a new instance of the Node class with the provided value
    5. Call the get method with the index minus 1 to retrieve the node before the desired index, and store the result in
    a variable, before
    6. Set a variable, after, to point to the next node after the before node
    7. Update the prev and next attributes of the new node to point to the before and after nodes, respectively
    8. Update the next attribute of the before node and the prev attribute of the after node to point to the new node
    9. Increment the length attribute of the linked list by 1
    10. Return True to indicate that the operation was successful
"""

from typing import Any, Optional


class Node:
    # Initializer AKA constructor
    def __init__(self, value: Any):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    # Initializer AKA constructor
    def __init__(self, value: Any):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def get(self, index: int) -> Optional[Node]:
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index: int, value: Any) -> bool:
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def append(self, value: Any) -> bool:
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value: Any) -> bool:
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop(self) -> Optional[Node]:
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def pop_first(self) -> Optional[Node]:
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def insert(self, index: int, value: Any) -> bool:
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True

    def print_list(self):
        if self.head is None:
            print("Empty linked list")
        else:
            values = []
            current_node = self.head
            values.append("None")
            while current_node:
                values.append(str(current_node.value))
                current_node = current_node.next
            values.append("None")
            print(" <-> ".join(values))


if __name__ == "__main__":
    my_doubly_linked_list = DoublyLinkedList(1)
    my_doubly_linked_list.append(3)

    print("DLL before insert():")
    my_doubly_linked_list.print_list()

    my_doubly_linked_list.insert(1, 2)

    print("\nDLL after insert(2) in middle:")
    my_doubly_linked_list.print_list()

    my_doubly_linked_list.insert(0, 0)

    print("\nDLL after insert(0) at beginning:")
    my_doubly_linked_list.print_list()

    my_doubly_linked_list.insert(4, 4)

    print("\nDLL after insert(4) at end:")
    my_doubly_linked_list.print_list()
