"""
Create a Stack class that represents a last-in, first-out (LIFO) data structure using a linked list implementation
- The Stack class should contain the following components:
    1. A Node class, which serves as the building block for the linked list - The Node class should have an __init__
    method that initializes the following attributes:
        - value: The value of the node
        - next: A reference to the next node in the linked list, initialized to None
    2. The Stack class should have an __init__ method that initializes the stack with a single node, using the given
    value - The __init__ method should perform the following tasks:
        - Create a new instance of the Node class using the provided value
        - Set the top attribute of the Stack class to point to the new node
        - Initialize a height attribute for the Stack class, which represents the current number of nodes in the stack,
        and set it to 1
"""

from typing import Any


class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value: Any):
        new_node = Node(value)
        self.top = new_node
        self.height = 1


if __name__ == "__main__":
    my_stack = Stack(4)

    print("Top:", my_stack.top.value)
    print("Height:", my_stack.height)

    """
    EXPECTED OUTPUT:
    ----------------
    Top: 4
    Height: 1
    """
