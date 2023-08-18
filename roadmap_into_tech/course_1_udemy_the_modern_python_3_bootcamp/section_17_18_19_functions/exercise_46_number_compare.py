"""
Write a function called number_compare
- This function takes in two parameters (both numbers)
    - If the first number is greater than the second, the function returns
    "First is greater"
    - If the second number is greater than the first, the function returns
    "Second is greater"
    - Otherwise the function returns "Numbers are equal"
"""


def number_compare(first: int, second: int) -> str:
    if first > second:
        return "First is greater"
    elif second > first:
        return "Second is greater"
    return "Numbers are equal"


print(number_compare(1, 1))
print(number_compare(1, 0))
print(number_compare(2, 4))
