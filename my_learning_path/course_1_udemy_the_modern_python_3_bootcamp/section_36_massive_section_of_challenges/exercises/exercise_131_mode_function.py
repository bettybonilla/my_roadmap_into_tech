"""
- Write a function called mode
    - This function accepts a list of numbers and returns the most frequent number in the list of numbers - You can
    assume that the mode will be unique
    - This is another trickier exercise - Don't feel bad if you get stuck or need to move on and come back later on!
- Ex:
    mode([2, 4, 1, 2, 3, 3, 4, 4, 5, 4, 4, 6, 4, 6, 7, 4])  # 4
"""

import collections


def mode(your_list: list[int]) -> int:
    count_nums = collections.Counter(your_list)
    # print(count_nums)
    max_value = max(count_nums)
    # print(max_value)
    for key, value in count_nums.items():
        if value == max_value:
            return key


if __name__ == "__main__":
    print(mode([2, 4, 1, 2, 3, 3, 4, 4, 5, 4, 4, 6, 4, 6, 7, 4]))
