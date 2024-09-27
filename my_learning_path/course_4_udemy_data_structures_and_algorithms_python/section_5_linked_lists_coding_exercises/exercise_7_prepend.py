"""
Implement the prepend method for the LinkedList class
- The prepend method should add a new node with a given value to the beginning of the linked list, updating the head
attribute and the length attribute accordingly
- Keep in mind the following requirements:
    1. The method should handle the cases where the linked list is empty and where the linked list already has one or
    more nodes
    2. The method should create a new node with the given value and add it to the beginning of the linked list
    3. The method should update the head attribute of the LinkedList correctly
    4. The method should update the length attribute of the LinkedList to reflect the addition of the new node
    5. The method should return True if the operation is successful
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

    def prepend(self, value: Any) -> bool:
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

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
    my_linked_list = LinkedList(2)
    my_linked_list.append(3)

    print("Before prepend():")
    print("----------------")
    print("Head:", my_linked_list.head.value)
    print("Tail:", my_linked_list.tail.value)
    print("Length:", my_linked_list.length, "\n")
    print("Linked List:")
    my_linked_list.print_list()

    my_linked_list.prepend(1)

    print("\nAfter prepend():")
    print("---------------")
    print("Head:", my_linked_list.head.value)
    print("Tail:", my_linked_list.tail.value)
    print("Length:", my_linked_list.length, "\n")
    print("Linked List:")
    my_linked_list.print_list()
