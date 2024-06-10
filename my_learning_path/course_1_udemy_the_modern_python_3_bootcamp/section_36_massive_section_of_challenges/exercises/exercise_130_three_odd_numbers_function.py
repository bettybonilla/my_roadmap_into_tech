"""
Write a function called three_odd_numbers which accepts a list of numbers and returns True if any three consecutive
numbers sum to an odd number
- Ex:
    three_odd_numbers([1, 2, 3, 4, 5])  # True
    three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])  # True
    three_odd_numbers([5, 2, 1])  # False
    three_odd_numbers([1, 2, 3, 3, 2])  # False
"""


def three_odd_numbers(your_list: list[int]) -> bool:
    window = []
    window_size = 3
    index = 0
    for i in range(index, len(your_list)):
        window.append(your_list[i])
        if len(window) > window_size:
            break
        for j in range(index + 1, len(your_list)):
            window.append(your_list[j])
            if len(window) > window_size:
                break
            for k in range(index + 2, len(your_list)):
                window.append(your_list[k])
                # print(window)
                if len(window) > window_size:
                    break
                if sum(window) % 2 == 1:
                    return True
                else:
                    window.pop(0)
    return False


# Alternative code using while loop
# def three_odd_numbers(your_list: list[int]) -> bool:
#     i, j, k = 0, 1, 2
#     while True:
#         if k >= len(your_list):
#             return False
#         if sum([your_list[i], your_list[j], your_list[k]]) % 2 == 1:
#             return True
#         i += 1
#         j += 1
#         k += 1


if __name__ == "__main__":
    print(three_odd_numbers([1, 2, 3, 4, 5]))
    print(three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0]))
    print(three_odd_numbers([5, 2, 1]))
    print(three_odd_numbers([1, 2, 3, 3, 2]))
