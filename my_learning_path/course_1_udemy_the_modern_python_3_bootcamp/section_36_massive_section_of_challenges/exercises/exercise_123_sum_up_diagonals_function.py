"""
Write a function called sum_up_diagonals which accepts an NxN list of lists and sums up the two main diagonals in the
array - The one from the upper left to the lower right, and the one from the upper right to the lower left
- Ex:
    list1 = [
      [1, 2],
      [3, 4],
    ]

    sum_up_diagonals(list1)  # 10

    list2 = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9],
    ]

    sum_up_diagonals(list2)  # 30

    list3 = [
      [4, 1, 0],
      [-1, -1, 0],
      [0, 0, 9],
    ]

    sum_up_diagonals(list3)  # 11

    list4 = [
      [1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10, 11, 12],
      [13, 14, 15, 16],
    ]

    sum_up_diagonals(list4)  # 68
"""


def sum_up_diagonals(your_nested_list: list[list[int]]) -> int:
    left_num_index = 0
    right_num_index = -1
    diagonals_sum = 0
    for l in your_nested_list:
        diagonals_sum += l[left_num_index]
        left_num_index += 1
        diagonals_sum += l[right_num_index]
        right_num_index += -1
    return diagonals_sum


list1 = [
    [1, 2],
    [3, 4],
]

list2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

list3 = [
    [4, 1, 0],
    [-1, -1, 0],
    [0, 0, 9],
]

list4 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]


if __name__ == "__main__":
    print(sum_up_diagonals(list1))
    print(sum_up_diagonals(list2))
    print(sum_up_diagonals(list3))
    print(sum_up_diagonals(list4))
