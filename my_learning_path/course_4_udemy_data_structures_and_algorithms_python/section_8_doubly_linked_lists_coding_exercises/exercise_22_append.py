"""
Extend the previously implemented DoublyLinkedList class by adding an append method that inserts a new node with a given
value at the end of the linked list
- The method should perform the following tasks:
    1. Create a new instance of the Node class with the provided value
    2. If the linked list is empty (i.e., the head is None), set the head and tail of the linked list to the newly
    created node
    3. If the linked list is not empty, perform the following steps:
        1. Set the next attribute of the current tail node to the new node
        2. Set the prev attribute of the new node to the current tail node
        3. Update the tail of the linked list to the new node
    4. Increment the length attribute of the linked list by 1
    5. Return True to indicate that the operation was successful
"""

from typing import Any


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
    my_doubly_linked_list.append(2)
    print("Head:", my_doubly_linked_list.head.value)
    print("Tail:", my_doubly_linked_list.tail.value)
    print("Length:", my_doubly_linked_list.length, "\n")

    print("Doubly Linked List:")
    my_doubly_linked_list.print_list()
