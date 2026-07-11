"""
The below shows how we can use the wraps function (@wraps decorator) from the functools.wraps module to preserve a
decorated function’s metadata
- NOTE: It is good practice to use the @wraps decorator on your wrapper function especially if you plan on releasing
your code to the public
"""

from functools import wraps
from typing import Callable


def log_function_data(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> int:
        print(f"You are about to call {func.__name__}")
        print(f"Here's the documentation: {func.__doc__}")
        return func(*args, **kwargs)

    return wrapper


@log_function_data
def add_nums(num1: int, num2: int) -> int:
    """Add two numbers together."""
    return num1 + num2


if __name__ == "__main__":
    print(add_nums(10, 30))
    print("")
    print(add_nums.__name__)
    print(add_nums.__doc__)
    print("")
    print(help(add_nums))
