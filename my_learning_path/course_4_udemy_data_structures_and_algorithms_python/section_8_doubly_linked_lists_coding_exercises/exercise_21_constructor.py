"""
Design and implement a Python program that defines two classes: Node and DoublyLinkedList
1. Create a class called Node which will represent a single node in a doubly-linked list - The class should have the
following attributes:
    1. value: The data contained in the node
    2. next: A reference to the next node in the linked list
    3. prev: A reference to the previous node in the linked list
2. Create a class called DoublyLinkedList which will represent a doubly-linked list - The class should have the
following attributes:
    1. head: A reference to the head (first) node of the linked list
    2. tail: A reference to the tail (last) node of the linked list
    3. length: An integer representing the number of nodes in the linked list
- When initializing a new instance of the DoublyLinkedList class, the user should provide a value for the first node
- The constructor should create a new instance of the Node class using the provided value and assign it as both the head
and tail of the linked list
- The length attribute should be initialized to 1, as the linked list contains one node at the beginning
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


if __name__ == "__main__":
    my_doubly_linked_list = DoublyLinkedList(7)
    print("Head:", my_doubly_linked_list.head.value)
    print("Tail:", my_doubly_linked_list.tail.value)
    print("Length:", my_doubly_linked_list.length)

    """
    EXPECTED OUTPUT:
    ----------------
    Head: 7
    Tail: 7
    Length: 1
    """
