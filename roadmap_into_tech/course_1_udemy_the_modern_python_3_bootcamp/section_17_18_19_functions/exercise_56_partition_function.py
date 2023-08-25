"""
Write a function called partition
- This function accepts a list and a callback function (which you can assume
returns True or False)
- The function should iterate over each element in the list and invoke the
callback function at each iteration
    - If the result of the callback function is True, the element should
    go into the first list (the "truthy" list)
    - If the result of the callback function is False, the element should
    go into the second list (the "falsy" list)
    - When it's finished, partition should return both lists inside of one
    larger list, like so:
    [truthy_list, falsy_list]
"""

from typing import Callable


# A callback function is a function that is passed as an argument to another
# function
# Below, the is_even function was already provided and will be passed as an
# argument in the partition function
def is_even(num: int) -> bool:
    return num % 2 == 0


# print(is_even(4))
# print(is_even(3))


# Using a for loop
def partition(your_list: list[int], is_even: Callable[[int], bool]) -> list[list]:
    truthy_list = []
    falsy_list = []

    for i in your_list:
        if is_even(i):
            truthy_list.append(i)
        else:
            falsy_list.append(i)

    return [truthy_list, falsy_list]


# Alternative code using list comprehension
# Remember that using a list comprehension will be more CPU efficient than
# using a for loop
# def partition(your_list: list[int], is_even: Callable[[int], bool]) -> list[list]:
#     return [
#         [i for i in your_list if is_even(i)],
#         [i for i in your_list if not is_even(i)],
#     ]


print(partition([1, 2, 3, 4], is_even))
