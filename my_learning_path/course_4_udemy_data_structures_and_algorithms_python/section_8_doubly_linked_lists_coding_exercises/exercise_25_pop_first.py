"""
Implement the pop_first method that removes the first node from the linked list and returns it
- The method should perform the following tasks:
    1. If the linked list is empty (i.e., the length is 0), return None
    2. Store a reference to the current head node in a temporary variable
    3. If the linked list has only one node (i.e., the length is 1), set both the head and tail of the linked list to
    None
    4. If the linked list has more than one node, perform the following steps:
        1. Update the head of the linked list to be the next node of the current head
        2. Set the prev attribute of the new head node to None
        3. Set the next attribute of the removed node (stored in the temporary variable) to None
    5. Decrement the length attribute of the linked list by 1
    6. Return the removed node (stored in the temporary variable)
"""

from typing import Any, Optional


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

    def prepend(self, value: Any) -> bool:
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop(self) -> Optional[Node]:
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def pop_first(self) -> Optional[Node]:
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

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
            print(" <-> ".join(values))


if __name__ == "__main__":
    my_doubly_linked_list = DoublyLinkedList(2)
    my_doubly_linked_list.append(1)

    # (2) Items - Returns 2 Node
    print(my_doubly_linked_list.pop_first().value)
    # (1) Item -  Returns 1 Node
    print(my_doubly_linked_list.pop_first().value)
    # (0) Items - Returns None
    print(my_doubly_linked_list.pop_first())
