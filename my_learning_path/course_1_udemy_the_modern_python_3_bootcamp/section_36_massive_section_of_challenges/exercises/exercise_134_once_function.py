"""
- Write a function called once
    - This function accepts a function and returns a new function that can only be invoked once
    - If the function is invoked more than once, it should return None
    - Hint: You will need to define a new function inside your once function and return that function - You can add
    properties to your inner function to see if it has run already
- Ex:
    def add(a, b):
        return a + b

    oneAddition = once(add)
    oneAddition(2, 2)  # 4
    oneAddition(2, 2)  # None
    oneAddition(12, 200)  # None
"""

from typing import Callable


def once(func: Callable[[int, int], int]) -> Callable[[int, int], int | None]:
    once.run_counter = 0

    def inner(num1: int, num2: int) -> int | None:
        once.run_counter += 1
        if once.run_counter <= 1:
            return func(num1, num2)
        return None

    return inner


if __name__ == "__main__":

    def add(a, b):
        return a + b

    oneAddition = once(add)
    print(oneAddition(2, 2))
    print(oneAddition(2, 2))
    print(oneAddition(12, 200))
