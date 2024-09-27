"""
Write a method called has_loop that is part of the LinkedList class
- The method should be able to detect if there is a cycle or loop present in the linked list
- You are required to use Floyd's cycle-finding algorithm AKA the "tortoise and the hare" algorithm to detect the loop
    - This algorithm uses two pointers: A slow pointer and a fast pointer
        - The slow pointer moves one step at a time, while the fast pointer moves two steps at a time
        - If there is a loop in the linked list, the two pointers will eventually meet at some point
        - If there is no loop, the fast pointer will reach the end of the linked list
- The method should follow these guidelines:
    1. Create two pointers, slow and fast, both initially pointing to the head of the linked list
    2. Traverse the linked list with the slow pointer moving one step at a time, while the fast pointer moves two steps
    at a time
    3. If there is a loop in the linked list, the fast pointer will eventually meet the slow pointer - If this occurs,
    the method should return True
    4. If the fast pointer reaches the end of the linked list or encounters a None value, it means there is no loop in
    the linked list - In this case, the method should return False
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
        self.tail = new_node
        self.length = 1

    def append(self, value: Any) -> bool:
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def has_loop(self) -> bool:
        slow = self.head
        fast = self.head
        while fast.next:
            fast = fast.next
            slow = slow.next
            if fast.next is None:
                return False
            fast = fast.next
            if fast.next == slow.next:
                return True


if __name__ == "__main__":
    my_linked_list_1 = LinkedList(1)
    my_linked_list_1.append(2)
    my_linked_list_1.append(3)
    my_linked_list_1.append(4)
    my_linked_list_1.tail.next = my_linked_list_1.head
    print(my_linked_list_1.has_loop())  # Output: True

    my_linked_list_2 = LinkedList(1)
    my_linked_list_2.append(2)
    my_linked_list_2.append(3)
    my_linked_list_2.append(4)
    print(my_linked_list_2.has_loop())  # Output: False
