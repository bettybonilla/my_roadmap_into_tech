"""
Write a function called intersection
- This function should accept two lists and return a list with the values that
are in both input lists
    - Ex:
        intersection([1, 2, 3], [2, 3, 4])  # [2, 3]
        intersection(['a','b','z'], ['x','y','z'])  # ['z']
"""

from typing import Any


# Using the & intersection set operator as well as double casting
def intersection(list1: list[Any], list2: list[Any]) -> list[Any]:
    return list(set(list1) & set(list2))


# Alternative code using list comprehension
# def intersection(list1: list[Any], list2: list[Any]) -> list[Any]:
#     return [item for item in list1 if item in list2]


# Alternative code using list comprehension and the & intersection operator
# def intersection(list1: list[Any], list2: list[Any]) -> list[Any]:
#     return [item for item in set(list1) & set(list2)]


print(intersection([1, 2, 3], [2, 3, 4]))
print(intersection(["a", "b", "z"], ["x", "y", "z"]))
