"""
Create a new method called reverse that reverses the order of the nodes in the linked list (i.e., the first node becomes
the last node, the second node becomes the second-to-last node, and so on)
- To do this, you'll need to traverse the linked list and change the direction of the pointers between the nodes so that
they point in the opposite direction
- Do not change the value of the nodes
- Once you've done this for all nodes, you'll also need to update the head and tail pointers to reflect the new order of
the nodes
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

    def reverse(self):
        current_node = self.head
        while current_node:
            temp_next = current_node.next
            current_node.next = current_node.prev
            current_node.prev = temp_next
            current_node = temp_next
        temp = self.head
        self.head = self.tail
        self.tail = temp

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
    my_doubly_linked_list.append(3)
    my_doubly_linked_list.append(4)
    my_doubly_linked_list.append(5)

    print("DLL before reverse():")
    my_doubly_linked_list.print_list()

    my_doubly_linked_list.reverse()

    print("\nDLL after reverse():")
    my_doubly_linked_list.print_list()

    """
    EXPECTED OUTPUT:
    ----------------
    DLL before reverse():
    1
    2
    3
    4
    5

    DLL after reverse():
    5
    4
    3
    2
    1
    """
