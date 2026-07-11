"""
Swap the values of the first and last node
- Method name: swap_first_last
- Note that the pointers to the nodes themselves are not swapped - Only their values are exchanged
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

    def swap_first_last(self):
        if self.length > 1:
            first_node_value = self.head.value
            last_node_value = self.tail.value
            self.head.value = last_node_value
            self.tail.value = first_node_value

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

    print("DLL before swap_first_last():")
    my_doubly_linked_list.print_list()

    my_doubly_linked_list.swap_first_last()

    print("\nDLL after swap_first_last():")
    my_doubly_linked_list.print_list()

    """
    EXPECTED OUTPUT:
    ----------------
    DLL before swap_first_last():
    1
    2
    3
    4

    DLL after swap_first_last():
    4
    2
    3
    1
    """
