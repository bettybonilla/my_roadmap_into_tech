"""
Below we’ve created a speed_test decorator using the standard decorator pattern boilerplate which includes the
@wraps decorator as good practice
- NOTE: Using the time.time module is not the most precise/accurate way of benchmarking - It is used here for example
purposes
"""

from functools import wraps
from time import time
from typing import Callable


def speed_test(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> int:
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f"Executing: {func.__name__}")
        print(f"Time Elapsed: {end_time - start_time}")
        return result

    return wrapper


@speed_test
def sum_nums_gen() -> int:
    # Using a generator expression
    return sum(x for x in range(90_000_000))


@speed_test
def sum_nums_list() -> int:
    # Using a list comprehension
    return sum([x for x in range(90_000_000)])


if __name__ == "__main__":
    print(sum_nums_gen())
    print("")
    print(sum_nums_list())
