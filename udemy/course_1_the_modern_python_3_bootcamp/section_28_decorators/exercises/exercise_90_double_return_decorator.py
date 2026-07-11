"""
- Write a function called double_return which accepts a function and returns another function
- double_return should decorate a function by returning two copies of the inner function's return value inside a list
- Ex:
    @double_return
    def add(x, y):
        return x + y

    add(1, 2)  # [3, 3]

    @double_return
    def greet(name):
        return "Hi, I'm " + name

    greet("Colt")  # ["Hi, I'm Colt", "Hi, I'm Colt"]
"""

from functools import wraps
from typing import Any, Callable


def double_return(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> list[Any]:
        result = func(*args, **kwargs)
        return [result, result]

    return wrapper


@double_return
def add(x: int, y: int) -> int:
    return x + y


@double_return
def greet(name: str) -> str:
    return "Hi, I'm " + name


if __name__ == "__main__":
    print(add(1, 2))
    print("")
    print(greet("Colt"))
