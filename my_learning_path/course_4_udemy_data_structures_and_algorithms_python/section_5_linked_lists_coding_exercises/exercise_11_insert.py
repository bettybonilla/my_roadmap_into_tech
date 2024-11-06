"""
Implement the insert method for the LinkedList class
- Method signature: def insert(self, index, value):
    - The insert method should take an integer index and a value as parameters and insert a new node with the given
    value at the specified index in the linked list
    - If the index is out of bounds, the method should return False - If the new node is successfully inserted, the
    method should return True
    - Keep in mind the following requirements:
        1. The method should handle edge cases, such as inserting a new node at the beginning or end of the linked list
        2. The method should utilize the prepend, append, and get methods for handling these edge cases
        3. The method should create a new node with the given value and insert it at the specified index
        4. The method should update the next attribute of the previous node to point to the new node
        5. The method should increment the length attribute of the LinkedList class
        6. The method should return True if the new node is successfully inserted
        7. If the index is out of bounds, the method should return False
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

    def get(self, index: int) -> Optional[Node]:
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index: int, value: Any) -> bool:
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

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

    def insert(self, index: int, value: Any) -> bool:
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

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
    my_linked_list = LinkedList(1)
    my_linked_list.append(3)

    print("LL before insert():")
    my_linked_list.print_list()

    my_linked_list.insert(1, 2)

    print("\nLL after insert(2) in middle:")
    my_linked_list.print_list()

    my_linked_list.insert(0, 0)

    print("\nLL after insert(0) at beginning:")
    my_linked_list.print_list()

    my_linked_list.insert(4, 4)

    print("\nLL after insert(4) at end:")
    my_linked_list.print_list()

    """
    EXPECTED OUTPUT:
    ----------------
    LL before insert():
    1
    3

    LL after insert(2) in middle:
    1
    2
    3

    LL after insert(0) at beginning:
    0
    1
    2
    3

    LL after insert(4) at end:
    0
    1
    2
    3
    4
    """
