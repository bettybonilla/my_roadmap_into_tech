"""
The below represents insertion sort in code
"""


def insertion_sort(your_list: list[int]):
    n = len(your_list)

    for i in range(1, n):
        key = your_list[i]
        j = i - 1

        # Compare key with each element on the left of it in the "sorted portion" and move elements over to the right to
        # make room to insert key in the correct position
        while j >= 0 and key < your_list[j]:
            your_list[j + 1] = your_list[j]
            j -= 1

        # Insert key in the correct position
        your_list[j + 1] = key


if __name__ == "__main__":
    data = [9, 5, 1, 4, 3]
    insertion_sort(data)
    print("Sorted list in ascending order")
    print(data)
