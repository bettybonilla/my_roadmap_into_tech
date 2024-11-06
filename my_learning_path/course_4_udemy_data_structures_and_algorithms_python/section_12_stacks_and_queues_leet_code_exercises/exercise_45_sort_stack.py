"""
- The sort_stack function takes a single argument, a Stack object
- The function should sort the elements in the stack in ascending order (the lowest value will be at the top of the
stack) using only one additional stack
- NOTE: This is not a method within the Stack class, this is a separate function - Indent all the way to the left
- This will use the Stack class we created in the previous coding exercise in addition to one other method
    - The function should use the pop, push, peek, and is_empty methods of the Stack object
- The function should perform the following tasks:
    1. Create a new instance of the Stack class called sorted_stack
    2. While the input stack is not empty, perform the following:
        - Pop the top element from the input stack and store it in a variable temp
        - While the sorted_stack is not empty and its top element is greater than temp, pop the top element from
        sorted_stack and push it back onto the input stack
        - Push the temp variable onto the sorted_stack
    3. Once the input stack is empty, transfer the elements back from sorted_stack to the input stack
        - To do this, while sorted_stack is not empty, pop the top element from sorted_stack and push it onto the input
        stack
- Overall, the function should have a time complexity of O(n^2), where n is the number of elements in the original
stack, due to the nested loops used to compare the elements - However, the function should only use one additional
stack, which could be useful in situations where memory is limited
"""

from typing import Any, Optional


class Stack:
    def __init__(self):
        self.stack_list = []

    def is_empty(self) -> bool:
        return len(self.stack_list) == 0

    def size(self) -> int:
        return len(self.stack_list)

    def peek(self) -> Optional[Any]:
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def push(self, value: Any):
        self.stack_list.append(value)

    def pop(self) -> Optional[Any]:
        if self.is_empty():
            return None
        return self.stack_list.pop()

    def print_stack(self):
        for i in self.stack_list[::-1]:
            print(i)


def sort_stack(input_stack: Stack):
    sorted_stack = Stack()
    while not input_stack.is_empty():
        temp = input_stack.pop()
        while not sorted_stack.is_empty() and sorted_stack.peek() > temp:
            input_stack.push(sorted_stack.pop())
        sorted_stack.push(temp)
    while not sorted_stack.is_empty():
        input_stack.push(sorted_stack.pop())


if __name__ == "__main__":
    my_stack = Stack()
    my_stack.push(3)
    my_stack.push(1)
    my_stack.push(5)
    my_stack.push(4)
    my_stack.push(2)

    print("Stack before sort_stack():")
    my_stack.print_stack()

    sort_stack(my_stack)

    print("\nStack after sort_stack:")
    my_stack.print_stack()

    """
    EXPECTED OUTPUT:
    ----------------
    Stack before sort_stack():
    2
    4
    5
    1
    3

    Stack after sort_stack:
    1
    2
    3
    4
    5
    """
