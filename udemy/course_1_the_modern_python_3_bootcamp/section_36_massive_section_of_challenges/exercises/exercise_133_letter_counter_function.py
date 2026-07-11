"""
- Write a function called letter_counter which accepts a string and returns a function
    - When the inner function is invoked it should accept a parameter which is a letter and the inner function should
    return the number of times that letter appears - This inner function should be case-insensitive
- Ex:
    counter = letter_counter('Amazing')
    counter('a')  # 2
    counter('m')  # 1

    counter2 = letter_counter('This Is Really Fun!')
    counter2('i')  # 2
    counter2('t')  # 1
"""

import collections
from typing import Callable


def letter_counter(string: str) -> Callable[[str], int]:
    string = string.lower()

    def inner(letter: str) -> int:
        nonlocal string
        letter = letter.lower()
        count_letters = collections.Counter(string)
        return count_letters.get(letter)

    return inner


if __name__ == "__main__":
    counter = letter_counter("Amazing")
    print(counter("a"))
    print(counter("m"))

    counter2 = letter_counter("This Is Really Fun!")
    print(counter2("i"))
    print(counter2("t"))
