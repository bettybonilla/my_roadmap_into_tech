"""
Write a function called sum_floats
- This function should accept a variable number of arguments
- The function should return the sum of all the parameters that are floats
- If there are no floats, the function should return 0
    - Ex:
        sum_floats(1.5, 2.4, 'awesome', [], 1)  # 3.9
        sum_floats(1, 2, 3, 4, 5)  # 0
"""

from typing import Any


def sum_floats(*args: Any) -> int | float:
    # Used a generator expression
    return sum((i for i in args if type(i) == float))


print(sum_floats(1.5, 2.4, "awesome", [], 1))
print(sum_floats(1, 2, 3, 4, 5))
