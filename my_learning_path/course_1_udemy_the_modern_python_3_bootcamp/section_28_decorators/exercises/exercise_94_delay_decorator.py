"""
- Write a function called delay which accepts a time and returns an inner function that accepts a function
- When used as a decorator, delay will wait to execute the function being decorated by the amount of time passed into it
- Before starting the timer, delay will also print a message informing the user that there will be a delay before the
decorated function is executed
- Hint: Take a look at the sleep() function from the built-in time module if you want to pause code execution for a
certain amount of time
- Ex:
    @delay(3)
    def say_hi():
        return "hi"

    say_hi()
    # should print the message "Waiting 3s before running say_hi" to the console
    # should then wait 3 seconds
    # finally, should invoke say_hi and return "hi"
"""

from functools import wraps
from time import sleep
from typing import Callable


def delay(value: int) -> Callable:
    def inner(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> str:
            print(f"Waiting {value}s before running {func.__name__}")
            sleep(value)
            return func(*args, **kwargs)

        return wrapper

    return inner


@delay(3)
def say_hi() -> str:
    return "hi"


if __name__ == "__main__":
    print(say_hi())
