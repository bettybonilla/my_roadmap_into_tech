"""
Write a function called list_check which accepts a list and returns True if each value in the list is a list
- Otherwise, the function should return False
- Ex:
    list_check([[], [1], [2,3], (1,2)])  # False
    list_check([1, True, [], [1], [2,3]])  # False
    list_check([[], [1], [2,3]])  # True
"""

from typing import Any


def list_check(your_list: list[Any]) -> bool:
    return all((type(i) == list for i in your_list))


if __name__ == "__main__":
    print(list_check([[], [1], [2, 3], (1, 2)]))
    print(list_check([1, True, [], [1], [2, 3]]))
    print(list_check([[], [1], [2, 3]]))
