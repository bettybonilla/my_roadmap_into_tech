"""
The below shows how we can enforce that a specific argument is passed first for a decorated function
"""

from functools import wraps
from typing import Any
from typing import Callable


def enforce_first_arg(value: Any) -> Callable:
    def inner(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            if args[0] == value:
                return func(*args, **kwargs)
            return f"First arg needs to be {value}!"

        return wrapper

    return inner


@enforce_first_arg("burrito")
def fav_foods(*foods: str) -> tuple[str, ...]:
    return foods


@enforce_first_arg(10)
def add_to_ten(num1: int, num2: int) -> int:
    return num1 + num2


if __name__ == "__main__":
    print(fav_foods("burrito", "pizza"))
    print(fav_foods("pizza", "burrito"))
    print("")
    print(add_to_ten(10, 12))
    print(add_to_ten(1, 2))
