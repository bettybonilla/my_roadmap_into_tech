"""
Write a function called sum_even_values
- This function should accept a variable number of arguments and return the
sum of all the arguments that are divisible by 2
- If there are no numbers divisible by 2, the function should return 0
- To be clear, it accepts all the numbers as individual arguments!
    - Ex:
        sum_even_values(1, 2, 3, 4, 5, 6)  # 12
        sum_even_values(4, 2, 1, 10)  # 16
        sum_even_values(1)  # 0
"""


def sum_even_values(*args: int) -> int:
    # Used a generator expression
    return sum((i for i in args if i % 2 == 0))


print(sum_even_values(1, 2, 3, 4, 5, 6))
print(sum_even_values(4, 2, 1, 10))
print(sum_even_values(1))
