"""
Below we've created a generator function
"""

from typing import Iterator


# A generator function that yields ints is secretly just a function that returns an iterator of ints
def count_up_to(max_num: int) -> Iterator[int]:
    count = 1

    while count <= max_num:
        yield count
        count += 1


# Unlike a regular function which will return the same result each time you run it, a generator function will store the
# most recent yield result in memory and then when you run it again, it will return the next yield result - Since it is
# a generator object, which is an iterator, you must keep using the next() function wrapped in a print() function
counter = count_up_to(5)
print(counter)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

# Will raise a StopIteration error
# print(next(counter))
