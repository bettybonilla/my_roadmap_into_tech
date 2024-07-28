"""
The below represents quick sort in code
"""


# Recursive function to perform quick sort
def quick_sort(your_list: list[int], low: int, high: int):
    if low < high:
        # Sets the partition index as the partition point
        partition_point = partition_index(your_list, low, high)

        # Recursive call on left side of partition point
        quick_sort(your_list, low, partition_point - 1)

        # Recursive call on right side of partition point
        quick_sort(your_list, partition_point + 1, high)


# Function to find the partition index
def partition_index(your_list: list[int], low: int, high: int) -> int:
    # Sets the rightmost element as the pivot element
    pivot = your_list[high]

    # Second pointer for a larger element
    i = low - 1

    # Compare each element with the pivot element from index 0 until the second to last element (the element before the
    # pivot element)
    for j in range(low, high):

        # Elements smaller than or equal to the pivot element are swapped towards the left
        if your_list[j] <= pivot:
            i += 1
            your_list[i], your_list[j] = your_list[j], your_list[i]

    # The pivot element is swapped with a larger element
    # Elements smaller than or equal to the pivot element are now on the left of the pivot element
    # Elements larger than the pivot element are now on the right of the pivot element
    your_list[i + 1], your_list[high] = your_list[high], your_list[i + 1]

    # The partition index where the partition is done and the pivot element was swapped
    return i + 1


if __name__ == "__main__":
    data = [8, 7, 2, 1, 0, 4, 9, 6]
    list_size = len(data)
    quick_sort(your_list=data, low=0, high=list_size - 1)
    print("List sorted in ascending order")
    print(data)
