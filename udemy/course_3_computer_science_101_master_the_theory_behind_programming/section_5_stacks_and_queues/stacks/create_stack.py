"""
The below represents a stack using a list in code
"""

from typing import Any, NoReturn, Optional


# Creates an empty stack
# To specify an empty list, you would use the NoReturn type hint in your function’s signature
def create_stack() -> list[NoReturn]:
    return []


# Checks if the stack is empty
def is_empty(your_stack: list[Any]) -> bool:
    return len(your_stack) == 0


# Adds an item/element to the top of the stack
def push(your_stack: list[Any], item: Any):
    your_stack.append(item)
    print(f"{item} was added to the top of the stack")


# Removes an item/element from the top of the stack
def pop(your_stack: list[Any]) -> Optional[Any]:
    if is_empty(your_stack):
        return None
    return your_stack.pop()


if __name__ == "__main__":
    stack = create_stack()
    print(stack)
    push(stack, 4)
    push(stack, 7)
    print(stack)
    print("popped item:", pop(stack))
    print("empty stack?", is_empty(stack))
    print(stack)
    print("popped item:", pop(stack))
    print("empty stack?", is_empty(stack))
    print(stack)
