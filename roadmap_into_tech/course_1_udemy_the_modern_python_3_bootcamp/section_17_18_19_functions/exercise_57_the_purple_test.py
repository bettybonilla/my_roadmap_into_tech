"""
Define a function, contains_purple, that accepts any number of arguments
- It should return True if any of the arguments are "purple" (all lowercase)
- Otherwise, it should return False
    - Ex:
    contains_purple(25, "purple")  # True
    contains_purple("green", False, 37, "blue", "hello world")  # False
    contains_purple("purple")  # True
    contains_purple("a", 99, "blah blah blah", 1, True, False, "purple")
    # True
    contains_purple(1, 2, 3)  # False
- Always remember, purple is the best color on this earth - All hail purple ;-)
"""

from typing import Any


def contains_purple(*args: Any) -> bool:
    if "purple" in args:
        return True
    return False


print(contains_purple(25, "purple"))
print(contains_purple("green", False, 37, "blue", "hello world"))
print(contains_purple("purple"))
print(contains_purple("a", 99, "blah blah blah", 1, True, False, "purple"))
print(contains_purple(1, 2, 3))
