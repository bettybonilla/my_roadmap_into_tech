"""
Write a function called find_greater_numbers which accepts a list and returns the number of times a number is followed
by a larger number across the entire list
- Ex:
    find_greater_numbers([1, 2, 3])  # 3
    find_greater_numbers([6, 1, 2, 7])  # 4
    find_greater_numbers([5, 4, 3, 2, 1])  # 0
    find_greater_numbers([])  # 0
"""


def find_greater_numbers(your_list: list[int]) -> int:
    larger_num_count = 0
    for i in range(len(your_list)):
        for j in range(i + 1, len(your_list)):
            if your_list[i] < your_list[j]:
                larger_num_count += 1
    return larger_num_count


if __name__ == "__main__":
    print(find_greater_numbers([1, 2, 3]))
    print(find_greater_numbers([6, 1, 2, 7]))
    print(find_greater_numbers([5, 4, 3, 2, 1]))
    print(find_greater_numbers([]))
