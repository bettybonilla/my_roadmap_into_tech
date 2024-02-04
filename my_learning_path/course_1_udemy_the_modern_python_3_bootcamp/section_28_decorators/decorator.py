"""
The below shows how to make a decorator
"""

from typing import Callable


def be_polite(fn: Callable) -> Callable:
    def wrapper():
        print("What a pleasure to meet you!")
        print(fn())
        print("Have a great day!")

    return wrapper


@be_polite
def greet() -> str:
    return "My name is Colt"


@be_polite
def rage() -> str:
    return "I hate you!"


if __name__ == "__main__":
    greet()
    print("")
    rage()
