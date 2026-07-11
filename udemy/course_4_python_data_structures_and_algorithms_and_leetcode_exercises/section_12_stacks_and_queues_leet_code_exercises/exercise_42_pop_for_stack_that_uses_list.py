"""
Add a method to pop a value from the Stack implementation that we began in the last two Coding Exercises
"""

from typing import Any, Optional


class Stack:
    def __init__(self):
        self.stack_list = []

    def is_empty(self) -> bool:
        return len(self.stack_list) == 0

    def push(self, value: Any):
        self.stack_list.append(value)

    def pop(self) -> Optional[Any]:
        if self.is_empty():
            return None
        return self.stack_list.pop()

    def print_stack(self):
        for i in self.stack_list[::-1]:
            print(i)


if __name__ == "__main__":
    my_stack = Stack()
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)

    print("Stack before pop():")
    my_stack.print_stack()

    print("\nPopped node:")
    print(my_stack.pop())

    print("\nStack after pop():")
    my_stack.print_stack()

    """
    EXPECTED OUTPUT:
    ----------------
    Stack before pop():
    3
    2
    1

    Popped node:
    3

    Stack after pop():
    2
    1
    """
