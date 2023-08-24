"""
Write a function called compact
- This function accepts a list and returns a list of values that are truthy
values without any of the falsy values
    - Ex:
    1. compact([0, 1, 2, "", [], False, {}, None, "All done"])  # [1, 2,
    "All done"]
"""

from typing import Any


def compact(your_list: list[Any]) -> list[Any]:
    return [i for i in your_list if bool(i)]
    # The code below has been refactored to the code above
    # The == True is not needed and Python will mark it as a problem
    # return [i for i in your_list if bool(i) == True]


# Alternative code without bool() function
# def compact(your_list: list[Any]) -> list[Any]:
#     return [i for i in your_list if i]


print(compact([0, 1, 2, "", [], False, {}, None, "All done"]))
