"""
Given an unsorted array of integers, write a function that finds the length of the longest_consecutive_sequence
(i.e., sequence of integers in which each element is one greater than the previous element)
- Use sets to optimize the runtime of your solution
    - Input:
        - An unsorted array of integers, nums
    - Output:
        - An integer representing the length of the longest consecutive sequence in nums
- Ex:
    Input: nums = [100, 4, 200, 1, 3, 2]
    Output: 4
    Explanation: The longest consecutive sequence in the input array is [4, 3, 2, 1], and its length is 4.
"""


def longest_consecutive_sequence(nums: list[int]) -> int:
    if not nums:
        return 0

    my_set = set(nums)
    my_list = list(my_set)
    my_list.sort()
    longest_consecutive_length = 0
    current_consecutive_length = 1
    for i in my_list:
        current_num = i
        if current_num + 1 in my_list:
            current_consecutive_length += 1
        if current_num + 1 not in my_list and current_consecutive_length > longest_consecutive_length:
            longest_consecutive_length = current_consecutive_length
            current_consecutive_length = 1
    return longest_consecutive_length


if __name__ == "__main__":
    print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))
    print(longest_consecutive_sequence([100, 200, 1, 3]))
    print(longest_consecutive_sequence([]))
    print(longest_consecutive_sequence([1, 3, 2, 5, 6, 7, 8]))
    print(longest_consecutive_sequence([-3, -2, -1, 0, 1, 2]))

    """
    EXPECTED OUTPUT:
    ----------------
    4
    1
    0
    4
    6
    """
