"""
Write a function called get_multiples which accepts a number and a count and returns a generator that yields the first
count multiples of the number - The default number should be 1 and the default count should be 10
- Ex:
    evens = get_multiples(2, 3)
    next(evens)  # 2
    next(evens)  # 4
    next(evens)  # 6
    next(evens)  # StopIteration

    default_multiples = get_multiples()
    list(default_multiples)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""

from typing import Iterator


def get_multiples(number: int = 1, count: int = 10) -> Iterator[int]:
    counter = 1

    while counter <= count:
        multiple = number * counter
        yield multiple
        counter += 1


evens = get_multiples(2, 3)
print(next(evens))
print(next(evens))
print(next(evens))
# Raises StopIteration error
# print(next(evens))

default_multiples = get_multiples()
print(list(default_multiples))
