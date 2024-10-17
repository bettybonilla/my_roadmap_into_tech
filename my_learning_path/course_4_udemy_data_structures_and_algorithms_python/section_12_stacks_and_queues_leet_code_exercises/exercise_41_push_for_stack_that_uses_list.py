"""
Add a method to push a value onto the Stack implementation that we began in the last Coding Exercise
"""

from typing import Any


class Stack:
    def __init__(self):
        self.stack_list = []

    def push(self, value: Any):
        self.stack_list.append(value)

    def print_stack(self):
        for i in self.stack_list[::-1]:
            print(i)


if __name__ == "__main__":
    my_stack = Stack()
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)

    my_stack.print_stack()
