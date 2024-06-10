"""
- Write a function called next_prime which returns a generator that will yield an unlimited number of primes starting
from the first prime (2)
    - Recall that a prime number is any whole number that has exactly two divisors: 1 and the number itself
    - The first few primes are 2, 3, 5, 7, 11, etc.
- Ex:
    primes = next_prime()
    [next(primes) for i in range(25)]
    # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
"""

from typing import Iterator


def next_prime() -> Iterator[int]:
    num = 2
    prime = True

    while True:
        for i in range(2, num):
            if num % i == 0:
                prime = False
                num += 1
                break
            else:
                prime = True
        if prime:
            yield num
            num += 1


if __name__ == "__main__":
    primes = next_prime()
    print([next(primes) for i in range(25)])
