"""
Write a method to determine whether a given doubly-linked list reads the same forwards and backwards
- Ex:
    - If the linked list contains the values [1, 2, 3, 2, 1] then the method should return True since the linked list is
    a palindrome
    - If the linked list contains the values [1, 2, 3, 4, 5] then the method should return False since the linked list
    is not a palindrome
- Method name: is_palindrome
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

    def is_palindrome(self) -> bool:
        # All single digits are considered palindromes in a base 10 system: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
        if self.length <= 1:
            return True
        list1 = []
        temp = self.head
        for _ in range(self.length):
            list1.append(temp.value)
            temp = temp.next
        if list1 == list1[::-1]:
            return True
        return False

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

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0


if __name__ == "__main__":
    my_dll_1 = DoublyLinkedList(1)
    my_dll_1.append(2)
    my_dll_1.append(3)
    my_dll_1.append(2)
    my_dll_1.append(1)

    print("my_dll_1 is_palindrome:")
    print(my_dll_1.is_palindrome())

    my_dll_1.make_empty()
    print("\nmy_dll_1 is_palindrome:")
    print(my_dll_1.is_palindrome())

    my_dll_2 = DoublyLinkedList(1)
    my_dll_2.append(2)
    my_dll_2.append(3)

    print("\nmy_dll_2 is_palindrome:")
    print(my_dll_2.is_palindrome())
