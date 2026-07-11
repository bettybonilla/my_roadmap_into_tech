"""
Check to see if a string of parentheses is balanced or not
- By "balanced," we mean that for every open parenthesis, there is a matching closing parenthesis in the correct order
    - Examples
        - The string "((()))" has three pairs of balanced parentheses, so it is a balanced string
        - On the other hand, the string "(()))" has an imbalance, as the last two parentheses do not match, so it is not
        balanced
        - Also, the string ")(" is not balanced because the close parenthesis needs to follow the open parenthesis
- Your program should take a string of parentheses as input and return True if it is balanced, or False if it is not
- In order to solve this problem, use a Stack data structure - This will use the Stack class we created in the previous
coding exercise
- Function name: is_balanced_parentheses
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


def is_balanced_parentheses(string: str) -> bool:
    my_stack = Stack()
    for paren in string:
        my_stack.push(paren)
    if my_stack.size() % 2 == 1:
        return False
    if string == "":
        return True
    if my_stack.stack_list[0] == "(" and my_stack.stack_list[-1] == ")":
        return True
    return False


if __name__ == "__main__":

    def test_is_balanced_parentheses():
        try:
            assert is_balanced_parentheses("((()))") == True
            print("Test case 1 passed")
        except AssertionError:
            print("Test case 1 failed")

        try:
            assert is_balanced_parentheses("()") == True
            print("Test case 2 passed")
        except AssertionError:
            print("Test case 2 failed")

        try:
            assert is_balanced_parentheses("(()())") == True
            print("Test case 3 passed")
        except AssertionError:
            print("Test case 3 failed")

        try:
            assert is_balanced_parentheses("(()") == False
            print("Test case 4 passed")
        except AssertionError:
            print("Test case 4 failed")

        try:
            assert is_balanced_parentheses("())") == False
            print("Test case 5 passed")
        except AssertionError:
            print("Test case 5 failed")

        try:
            assert is_balanced_parentheses(")(") == False
            print("Test case 6 passed")
        except AssertionError:
            print("Test case 6 failed")

        try:
            assert is_balanced_parentheses("") == True
            print("Test case 7 passed")
        except AssertionError:
            print("Test case 7 failed")

        try:
            assert is_balanced_parentheses("()()()()") == True
            print("Test case 8 passed")
        except AssertionError:
            print("Test case 8 failed")

        try:
            assert is_balanced_parentheses("(())(())") == True
            print("Test case 9 passed")
        except AssertionError:
            print("Test case 9 failed")

        try:
            assert is_balanced_parentheses("(()()())") == True
            print("Test case 10 passed")
        except AssertionError:
            print("Test case 10 failed")

        try:
            assert is_balanced_parentheses("((())") == False
            print("Test case 11 passed")
        except AssertionError:
            print("Test case 11 failed")

    test_is_balanced_parentheses()
