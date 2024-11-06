"""
Implement a basic data structure, a singly-linked list
- To accomplish this, you will create two classes:
    - Node
    - LinkedList
- The Node class will represent an individual node within the linked list, while the LinkedList class will manage the
overall linked list structure
- Your implementation should satisfy the following requirements:
    1. Create a Node class with the following features:
        1. A constructor that takes a value as an argument and initializes the value attribute of the node
        2. A next attribute, initialized to None, which will store a reference to the next node in the linked list
    2. Create a LinkedList class with the following features:
        1. A constructor that takes a value as an argument, creates a new Node with that value, and initializes the head
        and tail attributes of the linked list to point to the new node
        2. A length attribute, initialized to 1, which represents the current number of nodes in the linked list
"""

from typing import Any


class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value: Any):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


if __name__ == "__main__":
    my_linked_list = LinkedList(4)
    print("Head:", my_linked_list.head.value)
    print("Tail:", my_linked_list.tail.value)
    print("Length:", my_linked_list.length)

    """
    EXPECTED OUTPUT:
    ----------------
    Head: 4
    Tail: 4
    Length: 1
    """
