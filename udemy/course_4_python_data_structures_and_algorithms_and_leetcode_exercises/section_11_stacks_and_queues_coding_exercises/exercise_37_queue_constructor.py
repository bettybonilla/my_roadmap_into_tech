"""
Create a Queue class that represents a first-in, first-out (FIFO) data structure using a linked list implementation
- The Queue class should contain the following components:
    1. A Node class, which serves as the building block for the linked list - The Node class should have an __init__
    method that initializes the following attributes:
        - value: The value of the node
        - next: A reference to the next node in the linked list, initialized to None
    2. The Queue class should have an __init__ method that initializes the queue with a single node, using the given
    value - The __init__ method should perform the following tasks:
        - Create a new instance of the Node class using the provided value
        - Set the first attribute of the Queue class to point to the new node
        - Set the last attribute of the Queue class to point to the new node
        - Initialize a length attribute for the Queue class, which represents the current number of nodes in the queue,
        and set it to 1
"""

from typing import Any


class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value: Any):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1


if __name__ == "__main__":
    my_queue = Queue(4)

    print("First:", my_queue.first.value)
    print("Last:", my_queue.last.value)
    print("Length:", my_queue.length)

    """
    EXPECTED OUTPUT:
    ----------------
    First: 4
    Last: 4
    Length: 1
    """
