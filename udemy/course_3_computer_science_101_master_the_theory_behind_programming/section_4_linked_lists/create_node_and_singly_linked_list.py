"""
The below represents a node and a singly-linked list in code

References
- https://www.geeksforgeeks.org/python-linked-list/
"""

from typing import Any


class Node:
    # Initializes the Node object
    def __init__(self, data: Any):
        # Initializes the data point
        self.data = data
        # Initializes the next link which points to null
        self.next = None


class SinglyLinkedList:
    # Initializes the SinglyLinkedList object
    def __init__(self):
        # Initializes the head node which points to null atm since it just needs to be initialized first
        self.head = None

    # Adds a new Node to the front of a SinglyLinkedList object
    def insert_to_front(self, data: Any):
        # Creates the new Node and saves the data point to it
        new_node = Node(data)
        # Points the new Node's next link to the head node which points to null atm
        new_node.next = self.head
        # Points the head node to the new Node
        self.head = new_node

    # Prints the data of each Node of the SinglyLinkedList object by traversing the singly-linked list (iterating
    # through the singly-linked list) with a while loop until the current_node reaches the end of the singly-linked list
    # and becomes None
    def display_singly_linked_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


if __name__ == "__main__":
    singly_linked_list = SinglyLinkedList()
    singly_linked_list.insert_to_front(6)
    print("head node:", singly_linked_list.head)
    print("head node data point:", singly_linked_list.head.data)
    print("head node next link:", singly_linked_list.head.next)
    print("")

    singly_linked_list.display_singly_linked_list()
    print("")

    # Now this new Node is at the front of the SinglyLinkedList object
    singly_linked_list.insert_to_front(72)
    print("head node:", singly_linked_list.head)
    print("head node data point:", singly_linked_list.head.data)
    print("head node next link:", singly_linked_list.head.next)
    print("next node data point:", singly_linked_list.head.next.data)
    print("next node next link:", singly_linked_list.head.next.next)
    print("")

    singly_linked_list.display_singly_linked_list()
