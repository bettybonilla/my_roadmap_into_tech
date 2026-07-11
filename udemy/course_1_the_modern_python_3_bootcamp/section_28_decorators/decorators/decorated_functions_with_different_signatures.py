"""
The below shows how to handle decorated functions with different signatures by using the standard decorator pattern of
having *args and **kwargs as parameters in your wrapper function
"""

from typing import Callable


def shout(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> str:
        return func(*args, **kwargs).upper()

    return wrapper


@shout
def greet(name: str) -> str:
    return f"Hi, I'm {name}"


@shout
def order(main: str, side: str) -> str:
    return f"Hi, I'd like the {main} with a side of {side}"


@shout
def lol() -> str:
    return "lol"


if __name__ == "__main__":
    print(greet("todd"))
    print(order("burger", side="fries"))
    print(lol())
