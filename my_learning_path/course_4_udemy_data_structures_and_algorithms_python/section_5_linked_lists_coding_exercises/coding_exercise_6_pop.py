"""
Your task is to implement the pop method for the LinkedList class
- The pop method should remove the last node (tail node) from the linked list and return the removed node - If the
linked list is empty, the method should return None
- After the last node is removed, the second-to-last node should become the new tail node of the linked list
- Additionally, if the linked list becomes empty after the pop operation, both the head and tail attributes should be
set to None
- Keep in mind the following requirements:
    1. The method should handle the cases where the linked list is empty, has only one node, or has multiple nodes
    2. The method should update the tail attribute of the LinkedList correctly
    3. The method should update the length attribute of the LinkedList to reflect the removal of the node
    4. The method should either return the removed node or None if the linked list is empty
"""

from typing import Any, Optional


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

    def append(self, value: Any):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self) -> Optional[Node]:
        if self.length == 0:
            return None
        temp = self.head
        prev = self.head
        while temp.next:
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def print_list(self):
        values = []
        current_node = self.head
        while current_node:
            values.append(str(current_node.value))
            current_node = current_node.next
        values.append("None")
        print(" -> ".join(values))

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0


if __name__ == "__main__":

    def check(expect, actual, message):
        print(message)
        print("EXPECTED:", expect)
        print("RETURNED:", actual)
        print("PASS" if expect == actual else "FAIL", "\n")

    print("\n----- Test: Pop on linked list with one node -----\n")
    linked_list = LinkedList(1)
    linked_list.print_list()
    popped_node = linked_list.pop()
    check(1, popped_node.value, "Value of popped node:")
    check(None, linked_list.head, "Head of linked list:")
    check(None, linked_list.tail, "Tail of linked list:")
    check(0, linked_list.length, "Length of linked list:")

    print("\n----- Test: Pop on linked list with multiple nodes -----\n")
    linked_list = LinkedList(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.print_list()
    popped_node = linked_list.pop()
    check(3, popped_node.value, "Value of popped node:")
    check(1, linked_list.head.value, "Head of linked list:")
    check(2, linked_list.tail.value, "Tail of linked list:")
    check(2, linked_list.length, "Length of linked list:")

    print("\n----- Test: Pop on empty linked list -----\n")
    linked_list = LinkedList(1)
    linked_list.head = None
    linked_list.tail = None
    linked_list.length = 0
    popped_node = linked_list.pop()
    check(None, popped_node, "Popped node from empty linked list:")
    check(None, linked_list.head, "Head of linked list:")
    check(None, linked_list.tail, "Tail of linked list:")
    check(0, linked_list.length, "Length of linked list:")

    print("\n----- Test: Pop all -----\n")
    linked_list = LinkedList(1)
    linked_list.append(2)
    linked_list.print_list()
    popped_node = linked_list.pop()
    check(2, popped_node.value, "Value of popped node (first pop):")
    check(1, linked_list.head.value, "Head of linked list (after first pop):")
    check(1, linked_list.tail.value, "Tail of linked list (after first pop):")
    check(1, linked_list.length, "Length of linked list (after first pop):")
    popped_node = linked_list.pop()
    check(1, popped_node.value, "Value of popped node (second pop):")
    check(None, linked_list.head, "Head of linked list (after second pop):")
    check(None, linked_list.tail, "Tail of linked list (after second pop):")
    check(0, linked_list.length, "Length of linked list (after second pop):")
    popped_node = linked_list.pop()
    check(None, popped_node, "Popped node from empty linked list (third pop):")
    check(None, linked_list.head, "Head of linked list (after third pop):")
    check(None, linked_list.tail, "Tail of linked list (after third pop):")
    check(0, linked_list.length, "Length of linked list (after third pop):")
