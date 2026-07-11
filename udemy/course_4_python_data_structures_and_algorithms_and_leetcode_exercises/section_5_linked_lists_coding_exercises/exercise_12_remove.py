"""
Implement the remove method for the LinkedList class
- The remove method should take an integer index as a parameter and remove the node at the specified index in the linked
list, returning the removed node
- If the index is out of bounds, the method should return None
- Keep in mind the following requirements:
    1. The method should handle edge cases, such as removing a node at the beginning or end of the linked list
    2. The method should utilize the pop_first() and pop() methods for handling these edge cases
    3. The method should use the get() method to find the node previous to the one to be removed
    4. The method should update the next attribute of the previous node to point to the node after the removed one
    5. The method should decrement the length attribute of the LinkedList class
    6. The method should return the removed node if the removal is successful
    7. If the index is out of bounds, the method should return None
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

    def remove(self, index: int) -> Optional[Node]:
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
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
    my_linked_list = LinkedList(1)
    my_linked_list.append(2)
    my_linked_list.append(3)
    my_linked_list.append(4)
    my_linked_list.append(5)

    print("LL before remove():")
    my_linked_list.print_list()

    print("\nRemoved node:")
    print(my_linked_list.remove(2).value)
    print("LL after remove() in middle:")
    my_linked_list.print_list()

    print("\nRemoved node:")
    print(my_linked_list.remove(0).value)
    print("LL after remove() of first node:")
    my_linked_list.print_list()

    print("\nRemoved node:")
    print(my_linked_list.remove(2).value)
    print("LL after remove() of last node:")
    my_linked_list.print_list()

    """
    EXPECTED OUTPUT:
    ----------------
    LL before remove():
    1
    2
    3
    4
    5

    Removed node:
    3
    LL after remove() in middle:
    1
    2
    4
    5

    Removed node:
    1
    LL after remove() of first node:
    2
    4
    5

    Removed node:
    5
    LL after remove() of last node:
    2
    4
    """
