"""
- The Fibonacci sequence is a sequence in which each number is the sum of the two preceding ones - This can become a
very large sequence of numbers depending on the Fibonacci sequence of a number
    - Ex: The Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, and so on
    - Ex: The Fibonacci sequence of F10 = 55 (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55)
        - You start counting at F0 = 0, F1 = 1, F2 = 1, F3 = 2, F4 = 3, F5 = 5, F6 = 8, etc.
- Below is the difference between using a function which stores the Fibonacci sequence of a number in a list vs. using a
generator function to get the Fibonacci sequence of a number
"""

import sys
from typing import Iterator


def fib_list(fib_num: int) -> list[int]:
    nums = []
    a = 0
    b = 1

    while len(nums) < fib_num:
        nums.append(b)
        a, b = b, a + b
    return nums


def fib_gen(fib_num: int) -> Iterator[int]:
    count = 0
    x = 0
    y = 1

    while count < fib_num:
        x, y = y, x + y
        yield x
        count += 1


list_func = fib_list(10)
# Shows the higher the number, the more memory is used
# list_func = fib_list(100)

print(list_func)
list_func_memory_bytes = sys.getsizeof(list_func)
print(f"list_func used {list_func_memory_bytes} bytes")
print("")

gen_func = fib_gen(10)
# Shows the higher the number, the more memory friendly
# gen_func = fib_gen(100)

for i in gen_func:
    print(i)

gen_func_memory_bytes = sys.getsizeof(gen_func)
print(f"gen_func used {gen_func_memory_bytes} bytes")
