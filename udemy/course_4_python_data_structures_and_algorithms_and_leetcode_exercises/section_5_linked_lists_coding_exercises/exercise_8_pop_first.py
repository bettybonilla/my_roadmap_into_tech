"""
Implement the pop_first method for the LinkedList class
- The pop_first method should remove the first node (head node) from the linked list, update the head attribute and the
length attribute accordingly, and return the removed node
- Keep in mind the following requirements:
    1. The method should handle the cases where the linked list is empty and where the linked list has one or more nodes
    2. The method should save a reference to the current head node before updating the head attribute
    3. The method should update the head attribute to the second node in the linked list
    4. The method should disconnect the removed node from the linked list by setting its next attribute to None
    5. The method should update the length attribute of the LinkedList to reflect the removal of the node
    6. If the linked list becomes empty after removing the node, the method should set the tail attribute of the
    LinkedList to None
    7. The method should return the removed node, or None if the linked list is empty
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

    def pop_first(self) -> Optional[Node]:
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
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
    my_linked_list.append(1)

    # (2) Items - Returns 2 Node
    print(my_linked_list.pop_first().value)
    # (1) Item -  Returns 1 Node
    print(my_linked_list.pop_first().value)
    # (0) Items - Returns None
    print(my_linked_list.pop_first())

    """
    EXPECTED OUTPUT:
    ----------------
    2
    1
    None
    """
