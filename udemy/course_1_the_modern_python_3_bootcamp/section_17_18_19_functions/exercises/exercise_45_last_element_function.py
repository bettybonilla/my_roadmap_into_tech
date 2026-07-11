"""
Write a function called last_element
- This function takes in one parameter (a list) and returns the last value in
the list
- It should return None if the list is empty
"""

from typing import Any


def last_element(your_list: list[Any]) -> Any | None:
    if your_list:
        return your_list[-1]
    return None


# Alternative code using len() function to sanity check invisible characters
# in an empty list
# def last_element(your_list: list) -> Any | None:
#     if len(your_list) != 0:
#         return your_list[-1]
#     return None


print(last_element([1, 2, 3]))
print(last_element(["dog", "cat", "bird"]))
print(last_element([True, False, True, False]))
print(last_element([1, False, "cat", True]))
print(last_element([]))
