"""
The below represents a stack in code
"""

from typing import Any, NoReturn, Optional


# Creates an empty stack
# To specify an empty list, you would use the NoReturn type hint in your function’s signature
def create_stack() -> list[NoReturn]:
    return []


# Checks if the stack is empty
def is_empty(your_stack: list[Any]) -> bool:
    return len(your_stack) == 0


# Inserts item/element to the front of the stack
def insert_to_front(your_stack: list[Any], item: Any):
    your_stack.insert(0, item)
    print(f"{item} was inserted to the front of the stack")


# Removes item/element at the front of the stack
def remove_from_front(your_stack: list[Any]) -> Optional[Any]:
    if is_empty(your_stack):
        return None
    return your_stack.pop(0)


if __name__ == "__main__":
    stack = create_stack()
    print(stack)
    insert_to_front(stack, 4)
    insert_to_front(stack, 7)
    print(stack)
    print(remove_from_front(stack))
    print(stack)
