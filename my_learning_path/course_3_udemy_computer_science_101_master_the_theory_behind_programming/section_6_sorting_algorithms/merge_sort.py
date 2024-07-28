"""
The below represents merge sort in code
"""


def merge_sort(your_list: list[int]):
    if len(your_list) > 1:

        # Sets the partition index as the middle where the data will be divided into two halves
        middle = len(your_list) // 2
        # Left side (first half) of subarray from middle (excludes middle)
        L = your_list[:middle]
        # Right side (second half) of subarray from middle (includes middle)
        R = your_list[middle:]

        # Recursively sort the two halves until there is a final sorted subarray for merge_sort(L) and a final sorted
        # subarray for merge_sort(R) then the code below will be applied one more time for a final sorted merged array
        merge_sort(L)
        merge_sort(R)

        i, j, k = 0, 0, 0

        # Until we reach the end of either L or R, pick the smaller element between L and R and place it in the correct
        # position in the sorted array
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                your_list[k] = L[i]
                i += 1
            else:
                your_list[k] = R[j]
                j += 1
            k += 1

        # If any elements remain in either L or R, put the remaining elements in the sorted array
        while i < len(L):
            your_list[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            your_list[k] = R[j]
            j += 1
            k += 1


if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10]
    merge_sort(data)
    print("List sorted in ascending order")
    print(data)
