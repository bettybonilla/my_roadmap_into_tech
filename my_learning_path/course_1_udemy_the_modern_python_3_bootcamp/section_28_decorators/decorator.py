"""
The below shows how to make a decorator
- NOTE: Using func as your parameter name and wrapper as your “wrapper” function name is the typical naming convention
when making decorators
"""

from typing import Callable


def be_polite(func: Callable) -> Callable:
    def wrapper():
        print("What a pleasure to meet you!")
        print(func())
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
