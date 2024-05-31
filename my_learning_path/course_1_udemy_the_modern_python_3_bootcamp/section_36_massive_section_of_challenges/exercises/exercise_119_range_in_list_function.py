"""
- Write a function called range_in_list which accepts a list and start and end indices, and returns the sum of the
values between (and including) the start and end index
    - If a start parameter is not passed in, it should default to zero
    - If an end parameter is not passed in, it should default to the last value in the list
    - Also, if the end argument is too large, the sum should still go through the end of the list
- Ex:
    range_in_list([1, 2, 3, 4], 0, 2)  # 6
    range_in_list([1, 2, 3, 4], 0, 3)  # 10
    range_in_list([1, 2, 3, 4], 1)  # 9
    range_in_list([1, 2, 3, 4])  # 10
    range_in_list([1, 2, 3, 4], 0, 100)  # 10
    range_in_list([], 0, 1)  # 0
"""


def range_in_list(
    your_list: list[int], start_index: int = 0, end_index: int = None
) -> int:
    if not end_index:
        return sum(your_list[start_index:])

    end_index = end_index + 1
    return sum(your_list[start_index:end_index])


if __name__ == "__main__":
    print(range_in_list([1, 2, 3, 4], 0, 2))
    print(range_in_list([1, 2, 3, 4], 0, 3))
    print(range_in_list([1, 2, 3, 4], 1))
    print(range_in_list([1, 2, 3, 4]))
    print(range_in_list([1, 2, 3, 4], 0, 100))
    print(range_in_list([], 0, 1))
