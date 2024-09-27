"""
Implement the find_middle_node method for the LinkedList class
- NOTE: This LinkedList implementation does not have a length member variable
- If the linked list has an even number of nodes, return the first node of the second half of the linked list
- Keep in mind the following requirements:
    - The method should use a two-pointer approach, where one pointer (slow) moves one node at a time and the other
    pointer (fast) moves two nodes at a time
    - When the fast pointer reaches the end of the linked list or has no next node, the slow pointer should be at the
    middle node of the linked list
    - The method should return the middle node when the number of nodes is odd or the first node of the second half of
    the linked list if the linked list has an even number of nodes
    - The method should only traverse the linked list once - In other words, you can only use one loop
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

    def append(self, value: Any) -> bool:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True

    def find_middle_node(self) -> Node:
        slow = self.head
        fast = self.head
        while fast.next:
            fast = fast.next
            slow = slow.next
            # Alternative code
            # If you are ONLY expecting a None falsy value in your conditional logic then you should use is None for
            # clarity and readability otherwise, you can use if not which encompasses all falsy values
            # if not fast.next:
            if fast.next is None:
                break
            fast = fast.next
        return slow


# Alternative code without requirements
# class Node:
#     def __init__(self, value: Any):
#         self.value = value
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self, value: Any):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1
#
#     def append(self, value: Any) -> bool:
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         self.length += 1
#         return True
#
#     def find_middle_node(self) -> Node:
#         state = ""
#         middle_node_position = 0
#         temp = self.head
#         if self.length % 2 == 1:
#             state = "odd"
#         if self.length % 2 == 0:
#             state = "even"
#         if state == "odd" or "even":
#             middle_node_position = self.length // 2 + 1
#         middle_node_index = middle_node_position - 1
#         for _ in range(middle_node_index):
#             temp = temp.next
#         return temp
#         # The code below has been refactored to the code above
#         # middle_node_position = 0
#         # temp = self.head
#         # if self.length % 2 == 1:
#         #     middle_node_position = self.length // 2 + 1
#         # if self.length % 2 == 0:
#         #     middle_node_position = self.length // 2 + 1
#         # middle_node_index = middle_node_position - 1
#         # for _ in range(middle_node_index):
#         #     temp = temp.next
#         # return temp


if __name__ == "__main__":
    my_linked_list = LinkedList(1)
    my_linked_list.append(2)
    my_linked_list.append(3)
    my_linked_list.append(4)
    my_linked_list.append(5)
    # my_linked_list.append(6)  # Output: 4

    print(my_linked_list.find_middle_node().value)
