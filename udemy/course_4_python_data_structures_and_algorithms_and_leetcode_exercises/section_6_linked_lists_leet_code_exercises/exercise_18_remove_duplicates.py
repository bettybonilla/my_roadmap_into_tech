"""
You are given a singly-linked list that contains integer values, where some of these values may be duplicated
- NOTE: This linked list class does NOT have a tail which will make this method easier to implement
- Your task is to implement a method called remove_duplicates() within the LinkedList class that removes all duplicate
values from the linked list
    - Your method should not create a new linked list, but rather modify the existing linked list in-place, preserving
    the relative order of the nodes
    - You can implement the remove_duplicates() method in two different ways:
        1. Using a Set - This approach will have a time complexity of O(n), where n is the number of nodes in the linked
        list - You are allowed to use the provided Set data structure in your implementation
        2. Without using a Set - This approach will have a time complexity of O(n^2), where n is the number of nodes in
        the linked list - You are not allowed to use any additional data structures for this implementation
- Ex:
    - Input:
        - LinkedList: 1 -> 2 -> 3 -> 1 -> 4 -> 2 -> 5
    - Output:
        - LinkedList: 1 -> 2 -> 3 -> 4 -> 5
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

    def remove_duplicates(self):
        set1 = set()
        temp = self.head
        for _ in range(self.length):
            set1.add(temp.value)
            temp = temp.next
        list1 = list(set1)
        self.make_empty()
        for i in list1:
            self.append(i)

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

    def test_remove_duplicates(linked_list, expected_values):
        print("Before: ", end="")
        linked_list.print_list()
        linked_list.remove_duplicates()
        print("After:  ", end="")
        linked_list.print_list()

        # Collect values from linked list after removal
        result_values = []
        node = linked_list.head
        while node:
            result_values.append(node.value)
            node = node.next

        # Determine if the test passes
        if result_values == expected_values:
            print("Test PASS\n")
        else:
            print("Test FAIL\n")

    # Test 1: List with no duplicates
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    test_remove_duplicates(ll, [1, 2, 3])

    # Test 2: List with some duplicates
    ll = LinkedList(1)
    ll.append(2)
    ll.append(1)
    ll.append(3)
    ll.append(2)
    test_remove_duplicates(ll, [1, 2, 3])

    # Test 3: List with all duplicates
    ll = LinkedList(1)
    ll.append(1)
    ll.append(1)
    test_remove_duplicates(ll, [1])

    # Test 4: List with consecutive duplicates
    ll = LinkedList(1)
    ll.append(1)
    ll.append(2)
    ll.append(2)
    ll.append(3)
    test_remove_duplicates(ll, [1, 2, 3])

    # Test 5: List with non-consecutive duplicates
    ll = LinkedList(1)
    ll.append(2)
    ll.append(1)
    ll.append(3)
    ll.append(2)
    ll.append(4)
    test_remove_duplicates(ll, [1, 2, 3, 4])

    # Test 6: List with duplicates at the end
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(3)
    test_remove_duplicates(ll, [1, 2, 3])

    # Test 7: Empty list
    ll = LinkedList(None)
    ll.head = None  # Directly setting the head to None
    ll.length = 0  # Adjusting the length to reflect an empty list
    test_remove_duplicates(ll, [])
