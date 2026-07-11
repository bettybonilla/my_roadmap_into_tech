"""
- Write a function called enforce_fewer_than_three_args which accepts a function and returns another function
- The function passed to it should only be invoked if there are fewer than three positional arguments passed to it
    - Otherwise, the inner function should return "Too many arguments!"
- Ex:
    @enforce_fewer_than_three_args
    def add_all(*nums):
        return sum(nums)

    add_all()  # 0
    add_all(1)  # 1
    add_all(1, 2)  # 3
    add_all(1, 2, 3)  # "Too many arguments!"
    add_all(1, 2, 3, 4, 5, 6)  # "Too many arguments!"
"""

from functools import wraps
from typing import Callable


def enforce_fewer_than_three_args(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> int | str:
        if len(args) < 3:
            return func(*args, **kwargs)
        return "Too many arguments!"

    return wrapper


@enforce_fewer_than_three_args
def add_all(*nums: int) -> int:
    return sum(nums)


if __name__ == "__main__":
    print(add_all())
    print(add_all(1))
    print(add_all(1, 2))
    print(add_all(1, 2, 3))
    print(add_all(1, 2, 3, 4, 5, 6))
