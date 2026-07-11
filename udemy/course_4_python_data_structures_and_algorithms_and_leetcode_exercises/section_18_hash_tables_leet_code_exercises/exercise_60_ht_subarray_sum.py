"""
Given an array of integers nums and a target integer target, write a Python function called subarray_sum that finds the
indices of a contiguous subarray in nums that add up to the target sum using a hash table (dictionary)
- Your function should take two arguments:
    - nums: a list of integers representing the input array
    - target: an integer representing the target sum
- Your function should return a list of two integers representing the starting and ending indices of the subarray that
adds up to the target sum - If there is no such subarray, your function should return an empty list
- Ex:
    nums = [1, 2, 3, 4, 5]
    target = 9
    print(subarray_sum(nums, target))  # should print [1, 3]
- NOTE: There may be multiple subarrays that add up to the target sum, but your function only needs to return the
indices of any one such subarray. Also, the input list may contain both positive and negative integers.
"""

from typing import NoReturn


def subarray_sum(nums_list: list[int], target_num: int) -> list[int | NoReturn]:
    my_dict = {}
    for index, num in enumerate(nums_list):
        my_dict[index] = num
    # print(my_dict)
    my_list = []
    window_start = 0
    window_count = 0
    num_sum = 0
    while window_start < len(nums_list):
        my_list.append(window_start)
        for key, value in my_dict.items():
            num_sum += value
            if window_count > 0:
                window_count -= 1
                num_sum -= my_dict[window_count]
            if key == len(nums_list) - 1:
                my_list = []
                window_start += 1
                window_count += 1
                num_sum = 0
                break
            if num_sum == target_num:
                my_list.append(key)
                return my_list
    return []


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    target = 9
    print(subarray_sum(nums, target))

    nums = [-1, 2, 3, -4, 5]
    target = 0
    print(subarray_sum(nums, target))

    nums = [2, 3, 4, 5, 6]
    target = 3
    print(subarray_sum(nums, target))

    nums = []
    target = 0
    print(subarray_sum(nums, target))

    """
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []
    """
