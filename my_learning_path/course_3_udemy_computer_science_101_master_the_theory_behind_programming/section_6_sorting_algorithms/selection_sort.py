"""
The below represents selection sort in code
"""


def selection_sort(your_list: list[int]):
    n = len(your_list)

    # Loop through the list n times according to the number of elements in the list
    for i in range(0, n):

        # The first element in the "unsorted portion" in each iteration is assigned as the minimum
        min_index = i

        # Loop through the remaining elements in the list to compare elements
        for j in range(i + 1, n):

            # Compare which element is smaller
            if your_list[j] < your_list[min_index]:

                # Assign the smaller element as the new minimum
                min_index = j

        # Swapping occurs after all comparisons in each iteration if elements are not in the intended order
        # Therefore after each iteration, the minimum is placed in the "sorted portion" by swapping places with the next
        # element in the "unsorted portion"
        your_list[i], your_list[min_index] = your_list[min_index], your_list[i]


if __name__ == "__main__":
    data = [-2, 45, 0, 11, -9]
    selection_sort(data)
    print("Sorted list in ascending order")
    print(data)
