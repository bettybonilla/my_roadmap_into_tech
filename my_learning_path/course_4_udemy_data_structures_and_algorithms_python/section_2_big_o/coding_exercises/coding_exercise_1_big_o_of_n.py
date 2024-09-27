"""
Implement a Python function called print_items
- This function should take a single integer as an argument and print out a sequence of numbers from 0 up to, but not
including, the provided integer
- The function should use a for loop and Python's built-in range() function to generate the sequence of numbers
- The function signature should be: def print_items(n):
- Ex:
    - If you call print_items(10), your function should print:
        0
        1
        2
        3
        4
        5
        6
        7
        8
        9
"""


def print_items(n: int):
    for i in range(n):
        print(i)


if __name__ == "__main__":
    print_items(10)
