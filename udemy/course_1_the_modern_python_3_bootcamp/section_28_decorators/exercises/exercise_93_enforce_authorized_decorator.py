"""
- Write a function called enforce_authorized which accepts a function and returns another function
- The function passed to it should only be invoked if there exists a keyword argument with a name of "role" and a value
of "admin"
    - Otherwise, the inner function should return "Unauthorized"
- Ex:
    @enforce_authorized
    def show_secrets(*args, **kwargs):
        return "Shh! Don't tell anybody!"

    show_secrets(role="admin")  # "Shh! Don't tell anybody!"
    show_secrets(role="nobody")  # "Unauthorized"
    show_secrets(a="b")  # "Unauthorized"
"""

from functools import wraps
from typing import Callable


def enforce_authorized(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> str:
        for key, value in kwargs.items():
            if kwargs == {"role": "admin"}:
                return func(*args, **kwargs)
        return "Unauthorized"

    # Alternative code using any() function
    # @wraps(func)
    # def wrapper(*args, **kwargs) -> str:
    #     if any(
    #         {key: value for key, value in kwargs.items() if kwargs == {"role": "admin"}}
    #     ):
    #         return func(*args, **kwargs)
    #     return "Unauthorized"

    # Alternative code using .get() method
    # @wraps(func)
    # def wrapper(*args, **kwargs) -> str:
    #     if kwargs.get("role") == "admin":
    #         return func(*args, **kwargs)
    #     return "Unauthorized"

    return wrapper


@enforce_authorized
def show_secrets(*args, **kwargs) -> str:
    return "Shh! Don't tell anybody!"


if __name__ == "__main__":
    print(show_secrets(role="admin"))
    print(show_secrets(role="nobody"))
    print(show_secrets(a="b"))
