"""
Implement the get method for the DoublyLinkedList class that retrieves a node at a specific index in the linked list
- The method should perform the following tasks:
    1. If the given index is out of bounds (i.e., it is less than 0 or greater than or equal to the linked list length),
    return None
    2. Initialize a temporary variable, temp, to point to the head of the linked list
    3. If the index is less than half of the linked list length, iterate through the linked list from the head, updating
    the temp variable until the desired index is reached
    4. If the index is greater than or equal to half of the linked list length, start iterating from the tail of the
    linked list, updating the temp variable until the desired index is reached
    5. Return the node at the desired index (i.e., the temp variable)
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

    def print_list(self):
        if self.head is None:
            print("Empty linked list")
        else:
            values = []
            current_node = self.head
            while current_node:
                values.append(str(current_node.value))
                current_node = current_node.next
            values.append("None")
            print(" <-> ".join(values))


if __name__ == "__main__":
    my_doubly_linked_list = DoublyLinkedList(0)
    my_doubly_linked_list.append(1)
    my_doubly_linked_list.append(2)
    my_doubly_linked_list.append(3)

    print("Get node from first half of DLL:")
    print(my_doubly_linked_list.get(1).value)

    print("\nGet node from second half of DLL:")
    print(my_doubly_linked_list.get(2).value)
