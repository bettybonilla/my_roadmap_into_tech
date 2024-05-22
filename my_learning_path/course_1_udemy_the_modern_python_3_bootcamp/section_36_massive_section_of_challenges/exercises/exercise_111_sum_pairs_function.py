"""
Write a function called sum_pairs which accepts a list and a number and returns the first pair of numbers that sum to
the number passed to the function
- Ex:
    sum_pairs([4, 2, 10, 5, 1], 6)  # [4, 2]
    sum_pairs([11, 20, 4, 2, 1, 5], 100)  # []
- NOTE: This exercise is similar to the Two Sum LeetCode problem
- https://youtu.be/vNaCRT822ZE
"""

from typing import Any


# Using single for loop with a dictionary
def sum_pairs(your_list: list[int], target_sum: int) -> list[Any]:
    for i in your_list:
        complement_pair = {i: target_sum - i}
        if complement_pair.get(i) in your_list:
            return [i, complement_pair.get(i)]
    return []


# Alternative code using double for loop which is less memory efficient
# def sum_pairs(your_list: list[int], target_sum: int) -> list[Any]:
#     for i in range(len(your_list)):
#         for j in range(i + 1, len(your_list)):
#             if your_list[i] + your_list[j] == target_sum:
#                 return [your_list[i], your_list[j]]
#     return []


if __name__ == "__main__":
    print(sum_pairs([4, 2, 10, 5, 1], 6))
    print(sum_pairs([11, 20, 4, 2, 1, 5], 100))
