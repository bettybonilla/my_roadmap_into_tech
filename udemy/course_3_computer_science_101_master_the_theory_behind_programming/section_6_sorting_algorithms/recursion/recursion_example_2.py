"""
The below represents a recursive function to find the factorial of an integer

References
- https://www.programiz.com/python-programming/recursion
"""


def factorial(num: int) -> int:
    print(f"We are at: {num}")
    # Base case (exit condition)
    if num == 1:
        return 1
    # Recursive case
    else:
        return num * factorial(num - 1)


if __name__ == "__main__":
    print("The factorial of 3 is", factorial(3))
