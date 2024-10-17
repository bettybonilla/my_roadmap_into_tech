"""
Implement the pop method for the Stack class that removes the top node from the stack and returns it
- The method should perform the following tasks:
    1. If the stack is empty (i.e., the height is 0), return None
    2. Store a reference to the current top node in a temporary variable, temp
    3. Update the top attribute of the Stack class to point to the next node in the stack
    4. Set the next attribute of the removed node (stored in the temporary variable) to None
    5. Decrement the height attribute of the Stack class by 1
    6. Return the removed node (stored in the temporary variable)
"""

from typing import Any, Optional


class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value: Any):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def push(self, value: Any):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self) -> Optional[Node]:
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp

    def print_stack(self):
        if self.height == 0:
            print("Empty stack")
        else:
            temp = self.top
            while temp:
                print(temp.value)
                print("↓")
                temp = temp.next
            print("None")


if __name__ == "__main__":
    my_stack = Stack(4)
    my_stack.push(3)
    my_stack.push(2)
    my_stack.push(1)

    print("Stack before pop():")
    my_stack.print_stack()

    print("\nPopped node:")
    print(my_stack.pop().value)

    print("\nStack after pop():")
    my_stack.print_stack()
