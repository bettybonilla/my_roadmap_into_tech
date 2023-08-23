"""
Write a function called product that accepts two parameters and returns the
product of the two parameters (multiplies them together)
"""


def product(num1: int | float, num2: int | float) -> int | float:
    return num1 * num2


print(product(2, 2))
print(product(2, -2))
print(product(2.5, 2))
