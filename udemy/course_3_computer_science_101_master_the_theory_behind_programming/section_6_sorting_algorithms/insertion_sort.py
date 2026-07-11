"""
The below represents insertion sort in code
"""


def insertion_sort(your_list: list[int]):
    n = len(your_list)

    # Keep track of insertion
    insertion_ready = False

    for i in range(1, n):
        key = your_list[i]
        j = i - 1

        # Compare key with each element on the left of it in the "sorted portion" and move elements over to the right to
        # make room to insert key in the correct position
        while j >= 0 and key < your_list[j]:
            your_list[j + 1] = your_list[j]
            j -= 1

            # Keep track of insertion
            insertion_ready = True

        # Insert key in the correct position
        your_list[j + 1] = key

        # If no insertion occurred this means the list is already sorted therefore we can early escape
        if not insertion_ready:
            print("List is already sorted")
            break

    if insertion_ready:
        print("List sorted in ascending order")


if __name__ == "__main__":
    data = [9, 5, 1, 4, 3]
    # data = [1, 2, 3, 4, 5]
    insertion_sort(data)
    print(data)
