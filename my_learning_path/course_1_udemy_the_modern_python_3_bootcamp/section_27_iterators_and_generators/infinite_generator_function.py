"""
Below we've created an infinite generator function
"""

from typing import Iterator


# This infinite generator function will return the next yield result (beat) in a 4 count beat and avoids the
# StopIteration error
def current_beat() -> Iterator[int]:
    nums = (1, 2, 3, 4)
    i = 0

    while True:
        yield nums[i]
        i += 1
        if i >= len(nums):
            i = 0


counter = current_beat()
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
