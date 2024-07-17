"""
The below represents a recursive function in code
"""


def sum_by_3(n: int, x: int) -> int:
    print(f"We are at: {n}")
    # Base case (exit condition)
    if n <= 1:
        return x
    # Recursive case
    else:
        return sum_by_3(n - 3, x + n)


if __name__ == "__main__":
    print(sum_by_3(16, 0))
