"""
Write a function called remove_negatives that accepts a list of numbers and
returns a copy of the list with all the negative numbers removed
- Use the filter() function in your implementation, not a list comprehension!
    - Ex:
        remove_negatives([-1, 3, 4, -99])  # [3, 4]
        remove_negatives([-7, 0, 1, 2, 3, 4, 5])  # [0, 1, 2, 3, 4, 5]
        remove_negatives([50, 60, 70])  # [50, 60, 70]
- Make sure you return a list! - Remember filter does not return a list, you
have to convert the result to a list yourself
- NOTE: 0 is not considered negative so it should not be filtered out!
"""


def remove_negatives(nums: list[int]) -> list[int]:
    return list(filter(lambda x: x >= 0, nums))


# Alternative code using the not keyword to filter the numbers that are not
# negative numbers
# def remove_negatives(nums: list[int]) -> list[int]:
#     return list(filter(lambda x: not x < 0, nums))


print(remove_negatives([-1, 3, 4, -99]))
print(remove_negatives([-7, 0, 1, 2, 3, 4, 5]))
print(remove_negatives([50, 60, 70]))
