"""
Write a function called get_unlimited_multiples which accepts a number and returns a generator that will yield an
unlimited number of multiples of that number - The default number should be 1
- Ex:
    sevens = get_unlimited_multiples(7)
    [next(sevens) for i in range(15)]
    # [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105]

    ones = get_unlimited_multiples()
    [next(ones) for i in range(20)]
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
"""

from typing import Iterator


def get_unlimited_multiples(number: int = 1) -> Iterator[int]:
    counter = 1

    while True:
        multiple = number * counter
        yield multiple
        counter += 1


sevens = get_unlimited_multiples(7)
print([next(sevens) for i in range(15)])

ones = get_unlimited_multiples()
print([next(ones) for i in range(20)])
