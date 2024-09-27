"""
You are given a singly-linked list and two integers, start_index and end_index
- NOTE: The linked list does not have a tail which will make the implementation easier
- Your task is to write a method reverse_between within the LinkedList class that reverses the nodes of the linked list
from start_index to end_index (inclusive using 0-based indexing) in one pass and in-place
- Assumption: You can assume that start_index and end_index are not out of bounds
    - Input:
        - The method reverse_between takes two integer inputs, start_index and end_index
        - The method will only be passed valid indexes - You do not need to test whether the indexes are out of bounds
    - Output:
        - The method should modify the linked list in-place by reversing the nodes from start_index to end_index
        - If the linked list is empty or has only one node, the method should return None
- Ex:
    - Suppose the linked list is 1 -> 2 -> 3 -> 4 -> 5 and start_index = 2 and end_index = 4
    - Then, the method should modify the linked list to 1 -> 2 -> 5 -> 4 -> 3
- Constraints: The algorithm should run in one pass and in-place, with a time complexity of O(n) and a space complexity
of O(1)
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
        self.length = 1

    def append(self, value: Any):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1

    def reverse_between(self, start_index: int, end_index: int):
        if self.head is None or self.length == 1:
            return None
        list1 = []
        temp = self.head
        for _ in range(self.length):
            list1.append(temp.value)
            temp = temp.next
        self.make_empty()
        list2 = list1[start_index : end_index + 1]
        list2 = list2[::-1]
        list1[start_index : end_index + 1] = list2
        for i in list1:
            self.append(i)

    # Alternative code
    # def reverse_between(self, start_index: int, end_index: int):
    #     if self.length <= 1:
    #         return
    #     dummy_node = Node(0)
    #     dummy_node.next = self.head
    #     previous_node = dummy_node
    #     for _ in range(start_index):
    #         previous_node = previous_node.next
    #     current_node = previous_node.next
    #     for _ in range(end_index - start_index):
    #         node_to_move = current_node.next
    #         current_node.next = node_to_move.next
    #         node_to_move.next = previous_node.next
    #         previous_node.next = node_to_move
    #     self.head = dummy_node.next

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
            print(" -> ".join(values))

    def make_empty(self):
        self.head = None
        self.length = 0


if __name__ == "__main__":
    linked_list = LinkedList(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)

    print("Original linked list: ")
    linked_list.print_list()

    # Reverse a sublist within the linked list
    linked_list.reverse_between(2, 4)
    print("Reversed sublist (2, 4): ")
    linked_list.print_list()

    # Reverse another sublist within the linked list
    linked_list.reverse_between(0, 4)
    print("Reversed entire linked list: ")
    linked_list.print_list()

    # Reverse a sublist of length 1 within the linked list
    linked_list.reverse_between(3, 3)
    print("Reversed sublist of length 1 (3, 3): ")
    linked_list.print_list()

    # Reverse an empty linked list
    empty_list = LinkedList(0)
    empty_list.make_empty()
    empty_list.reverse_between(0, 0)
    print("Reversed empty linked list: ")
    empty_list.print_list()
