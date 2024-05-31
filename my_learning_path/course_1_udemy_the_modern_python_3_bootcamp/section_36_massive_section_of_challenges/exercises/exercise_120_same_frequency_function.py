"""
Write a function called same_frequency which accepts two numbers and returns True if they contain the same frequency of
digits
- Otherwise, it returns False
- Ex:
    same_frequency(551122, 221515)  # True
    same_frequency(321142, 3212215)  # False
    same_frequency(1212, 2211)  # True
"""

import collections


def same_frequency(num1: int, num2: int) -> bool:
    if collections.Counter(str(num1)) == collections.Counter(str(num2)):
        return True
    return False


if __name__ == "__main__":
    print(same_frequency(551122, 221515))
    print(same_frequency(321142, 3212215))
    print(same_frequency(1212, 2211))
