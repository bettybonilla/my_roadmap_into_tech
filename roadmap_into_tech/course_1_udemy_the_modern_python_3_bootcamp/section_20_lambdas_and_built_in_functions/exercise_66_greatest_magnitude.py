"""
Write a function max_magnitude that accepts a single list full of numbers
- It should return the magnitude of the number with the largest magnitude (the
number that is furthest away from zero)
    - Ex:
        max_magnitude([300, 20, -900])  # 900
        max_magnitude([10, 11, 12])  # 12
        max_magnitude([-5, -1, -89])  # 89
- Hint: Use the max() function and the abs() function!
"""


def max_magnitude(nums: list[int]) -> int:
    # Used a generator expression
    return max((abs(i) for i in nums))


print(max_magnitude([300, 20, -900]))
print(max_magnitude([10, 11, 12]))
print(max_magnitude([-5, -1, -89]))
