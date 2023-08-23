"""
Write a function called multiply_even_numbers
- This function accepts a list of numbers and returns the product of all even
numbers in the list
"""


def multiply_even_numbers(your_list: list[int]) -> int:
    even_numbers_product = 1

    for num in your_list:
        if num % 2 == 0:
            even_numbers_product *= num
    return even_numbers_product


print(multiply_even_numbers([1, 2, 3, 4, 5, 6]))
