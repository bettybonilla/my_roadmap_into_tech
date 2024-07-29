"""
The below represents bubble sort in code
"""


def bubble_sort(your_list: list[int]):
    n = len(your_list)

    # Keep track of swapping
    swapped = False

    # Loop through the list n times according to the number of elements in the list
    for i in range(0, n):

        # Loop through all elements in the list, minus the already sorted at the end, to compare elements
        for j in range(0, n - i - 1):

            # Compare the two adjacent elements
            if your_list[j] > your_list[j + 1]:

                # Swapping occurs after each comparison in each iteration if elements are not in the intended order
                # Therefore after each iteration, the largest element is placed at the end of the list
                your_list[j], your_list[j + 1] = your_list[j + 1], your_list[j]

                # Keep track of swapping
                swapped = True

        # If no swapping occurred this means the list is already sorted therefore we can early escape
        if not swapped:
            print("List is already sorted")
            break

    if swapped:
        print("List sorted in ascending order")


if __name__ == "__main__":
    data = [-2, 45, 0, 11, -9]
    # data = [1, 2, 3, 4, 5]
    bubble_sort(data)
    print(data)
