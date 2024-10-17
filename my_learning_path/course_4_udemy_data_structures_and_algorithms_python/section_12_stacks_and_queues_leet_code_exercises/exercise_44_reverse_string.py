"""
The reverse_string function takes a single argument string, which is the string you want to reverse
- Return a new string with the letters in reverse order
- This will use the Stack class we created in the previous coding exercise
- NOTE: This is not a method within the Stack class, this is a separate function - Indent all the way to the left
"""

from typing import Any, Optional


class Stack:
    def __init__(self):
        self.stack_list = []

    def is_empty(self) -> bool:
        return len(self.stack_list) == 0

    def size(self) -> int:
        return len(self.stack_list)

    def push(self, value: Any):
        self.stack_list.append(value)

    def pop(self) -> Optional[Any]:
        if self.is_empty():
            return None
        return self.stack_list.pop()

    def print_stack(self):
        for i in self.stack_list[::-1]:
            print(i)


def reverse_string(string: str) -> str:
    my_stack = Stack()
    my_stack.push(string)
    for i in my_stack.stack_list:
        return i[::-1]


if __name__ == "__main__":
    my_string = "hello"
    print(reverse_string(my_string))
