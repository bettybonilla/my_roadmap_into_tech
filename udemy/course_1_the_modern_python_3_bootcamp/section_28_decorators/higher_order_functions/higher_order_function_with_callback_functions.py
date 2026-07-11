"""
The below shows a higher order function which accepts one or more functions as an argument (callback function)
"""

from typing import Callable


# Adds the squares or cubes together (depending on which callback function you want to pass as the argument) up to n
# (exclusive)
def sum_nums(n: int, func: Callable) -> int:
    total = 0

    for num in range(n):
        total += func(num)
    return total


def square(x: int) -> int:
    return x * x


def cube(x: int) -> int:
    return x * x * x


# Will add the square of 0, 1, 2 which is 5 (0 + 1 + 4)
print(sum_nums(3, square))
# Will add the cube of 0, 1, 2 which is 9 (0 + 1 + 8)
print(sum_nums(3, cube))
