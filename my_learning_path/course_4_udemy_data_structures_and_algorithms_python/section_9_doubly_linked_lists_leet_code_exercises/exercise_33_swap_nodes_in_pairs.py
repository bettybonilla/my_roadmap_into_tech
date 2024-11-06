"""
You are given a doubly-linked list
- Implement a method called swap_pairs within the class that swaps the values of adjacent nodes in the linked list - The
method should not take any input parameters
- NOTE: This DoublyLinkedList does not have a tail pointer which will make the implementation easier
- Ex:
    - 1 <-> 2 <-> 3 <-> 4 should become 2 <-> 1 <-> 4 <-> 3
- Your implementation should handle edge cases such as an empty linked list or a linked list with only one node
- NOTE: You must solve the problem WITHOUT MODIFYING THE VALUES in the linked list's nodes (i.e., only the nodes’ prev
and next pointers may be changed)
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
        self.length = 1

    def append(self, value: Any) -> bool:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        self.length += 1
        return True

    def swap_pairs(self):
        if self.length > 1:
            dummy_node = Node(0)
            dummy_node.next = self.head
            previous_node = dummy_node
            while self.head and self.head.next:
                first_node = self.head
                second_node = self.head.next
                previous_node.next = second_node
                first_node.next = second_node.next
                second_node.next = first_node
                second_node.prev = previous_node
                first_node.prev = second_node
                if first_node.next:
                    first_node.next.prev = first_node
                    self.head = first_node.next
                    previous_node = first_node
            self.head = dummy_node.next
            self.head.prev = None

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
    my_dll = DoublyLinkedList(1)
    my_dll.append(2)
    my_dll.append(3)
    my_dll.append(4)

    print("my_dll before swap_pairs:")
    my_dll.print_list()

    my_dll.swap_pairs()

    print("\nmy_dll after swap_pairs:")
    my_dll.print_list()

    """
    EXPECTED OUTPUT:
    ----------------
    my_dll before swap_pairs:
    1 <-> 2 <-> 3 <-> 4
    
    my_dll after swap_pairs:
    2 <-> 1 <-> 4 <-> 3
    """
