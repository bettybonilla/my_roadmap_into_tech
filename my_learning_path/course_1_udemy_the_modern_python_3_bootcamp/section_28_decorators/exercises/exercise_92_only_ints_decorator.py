"""
- Write a function called only_ints which accepts a function and returns another function
- The function passed to it should only be invoked if all the arguments passed to it are integers
    - Otherwise, the inner function should return "Please only invoke with integers."
- Ex:
    @only_ints
    def add(x, y):
        return x + y

    add(1, 2)  # 3
    add("1", "2")  # "Please only invoke with integers."
"""

from functools import wraps
from typing import Callable


def only_ints(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> int | str:
        for i in args:
            if type(i) == int:
                return func(*args, **kwargs)
        return "Please only invoke with integers."

    # Alternative code using any() function
    # @wraps(func)
    # def wrapper(*args, **kwargs) -> int | str:
    #     if any([i for i in args if type(i) == int]):
    #         return func(*args, **kwargs)
    #     return "Please only invoke with integers."

    return wrapper


@only_ints
def add(x: int, y: int) -> int:
    return x + y


if __name__ == "__main__":
    print(add(1, 2))
    print(add("1", "2"))
