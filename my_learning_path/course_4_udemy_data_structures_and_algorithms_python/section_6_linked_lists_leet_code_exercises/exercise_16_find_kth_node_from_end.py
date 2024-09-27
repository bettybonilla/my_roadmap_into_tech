"""
Implement the find_kth_from_end function, which takes a LinkedList and an integer k as input, and returns the kth node
from the end of the linked list WITHOUT USING LENGTH
- Given this LinkedList:
    - 1 -> 2 -> 3 -> 4
- If k = 1 then return the first node from the end (the last node) which contains the value of 4
- If k = 2 then return the second node from the end which contains the value of 3, etc.
- If the index is out of bounds, the program should return None
- The find_kth_from_end function should follow these requirements:
    1. The function should utilize two pointers, slow and fast, initialized to the head of the linked list
    2. The fast pointer should move k nodes ahead in the linked list
    3. If the fast pointer becomes None before moving k nodes, the function should return None, as the linked list is
    shorter than k nodes
    4. The slow and fast pointers should then move forward in the linked list at the same time until the fast pointer
    reaches the end of the linked list
    5. The function should return the slow pointer, which will be at the kth position from the end of the linked list
- NOTE: This is a separate function that is not a method within the LinkedList class - This means you need to indent the
function all the way to the LEFT
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

    def append(self, value: Any) -> bool:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True


def find_kth_from_end(linked_list: LinkedList, k_value: int) -> Optional[Node]:
    slow = linked_list.head
    fast = linked_list.head
    for _ in range(k_value):
        fast = fast.next
        if fast is None:
            return None
    while fast:
        fast = fast.next
        slow = slow.next
    return slow


# Alternative code used only to pass most of instructor's improper tests
# def find_kth_from_end(linked_list: LinkedList, k_value: int) -> Node:
#     slow = linked_list.head
#     fast = linked_list.head
#     for _ in range(k_value):
#         fast = fast.next
#     while fast:
#         fast = fast.next
#         slow = slow.next
#     return slow


if __name__ == "__main__":
    my_linked_list = LinkedList(1)
    my_linked_list.append(2)
    my_linked_list.append(3)
    my_linked_list.append(4)
    my_linked_list.append(5)

    k = 2
    result = find_kth_from_end(my_linked_list, k)

    if result:
        print(result.value)
    if result is None:
        print(result)

    # Instructor's code
    # Raises an error when None is returned
    # AttributeError: 'NoneType' object has no attribute 'value'
    # print(result.value)  # Output: 4
