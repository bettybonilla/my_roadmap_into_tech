"""
Implement the prepend method that inserts a new node with a given value at the beginning of the linked list
- The method should perform the following tasks:
    1. Create a new instance of the Node class with the provided value
    2. If the linked list is empty (i.e., the length is 0), set the head and tail of the linked list to the newly
    created node
    3. If the linked list is not empty, perform the following steps:
        1. Set the next attribute of the new node to the current head node
        2. Set the prev attribute of the current head node to the new node
        3. Update the head of the linked list to the new node
    4. Increment the length attribute of the linked list by 1
    5. Return True to indicate that the operation was successful
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
    my_doubly_linked_list.append(3)

    print("Before prepend():")
    print("----------------")
    print("Head:", my_doubly_linked_list.head.value)
    print("Tail:", my_doubly_linked_list.tail.value)
    print("Length:", my_doubly_linked_list.length, "\n")
    print("Doubly Linked List:")
    my_doubly_linked_list.print_list()

    my_doubly_linked_list.prepend(1)

    print("\n\nAfter prepend():")
    print("---------------")
    print("Head:", my_doubly_linked_list.head.value)
    print("Tail:", my_doubly_linked_list.tail.value)
    print("Length:", my_doubly_linked_list.length, "\n")
    print("Doubly Linked List:")
    my_doubly_linked_list.print_list()
