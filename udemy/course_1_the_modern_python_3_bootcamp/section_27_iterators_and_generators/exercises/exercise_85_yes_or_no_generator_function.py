"""
Write a function called yes_or_no which returns a generator that first yields yes, then no, then yes, then no, and so on
- Ex:
    gen = yes_or_no()
    next(gen)  # 'yes'
    next(gen)  # 'no'
    next(gen)  # 'yes'
    next(gen)  # 'no'
"""

from typing import Iterator


def yes_or_no() -> Iterator[str]:
    yes_no = ["yes", "no"]

    while True:
        for i in yes_no:
            yield i


gen = yes_or_no()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
