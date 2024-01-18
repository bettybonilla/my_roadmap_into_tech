"""
Write a function called triple_and_filter
- This function should accept a list of numbers, filter out every number that
is not divisible by 4, and return a new list where every remaining number is
tripled
    - Ex:
        triple_and_filter([1, 2, 3, 4])  # [12]
        triple_and_filter([6, 8, 10, 12])  # [24, 36]
"""


# Using list comprehension
def triple_and_filter(nums: list[int]) -> list[int]:
    return [i * 3 for i in nums if i % 4 == 0]


# Alternative code using the map() function and filter() function
# def triple_and_filter(nums: list[int]) -> list[int]:
#     return list(
#         map(
#             lambda num: num * 3,
#             filter(lambda num: num % 4 == 0, nums),
#         )
#     )


print(triple_and_filter([1, 2, 3, 4]))
print(triple_and_filter([6, 8, 10, 12]))
