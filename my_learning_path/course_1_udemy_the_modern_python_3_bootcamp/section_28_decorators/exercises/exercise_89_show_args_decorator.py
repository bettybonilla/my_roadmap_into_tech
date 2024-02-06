"""
- Write a function called show_args which accepts a function and returns another function
- Before invoking the function passed to it, show_args should be responsible for printing two things:
    - A tuple of the positional arguments
    - A dictionary of the keyword arguments
- Ex:
    @show_args
    def do_nothing(*args, **kwargs):
        pass


    do_nothing(1, 2, 3, a="hi", b="bye")

    # Should print (on two lines):
    # Here are the args: (1, 2, 3)
    # Here are the kwargs: {"a": "hi", "b": "bye"}
"""

from functools import wraps
from typing import Callable


def show_args(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> None:
        print(f"Here are the args: {args}")
        print(f"Here are the kwargs: {kwargs}")
        return func(*args, **kwargs)

    return wrapper


@show_args
def do_nothing(*args, **kwargs) -> None:
    pass


if __name__ == "__main__":
    do_nothing(1, 2, 3, a="hi", b="bye")
