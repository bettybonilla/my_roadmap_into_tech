"""
The below shows another common use case for decorators which is to enforce restrictions on arguments
"""

from functools import wraps
from typing import Callable


def enforce_no_kwargs(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> str:
        if kwargs:
            raise ValueError("No kwargs allowed!")
        return func(*args, **kwargs)

    return wrapper


@enforce_no_kwargs
def greet(name: str) -> str:
    return f"Hi there {name}"


if __name__ == "__main__":
    print(greet("Ruby"))
    print("")
    print(greet(name="Ruby"))
