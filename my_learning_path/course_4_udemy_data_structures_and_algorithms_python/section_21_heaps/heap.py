"""
The below represents a max heap in code
"""

from typing import Optional


class MaxHeap:
    # Initializer AKA constructor
    def __init__(self):
        self.heap = []

    # Inserts a node in the MaxHeap object
    def insert(self, value: int):
        self.heap.append(value)
        current_index = len(self.heap) - 1
        while (
            current_index > 0
            and self.heap[current_index] > self.heap[self._parent(current_index)]
        ):
            self._swap(current_index, self._parent(current_index))
            current_index = self._parent(current_index)

    # Removes the root node in the MaxHeap object
    def remove(self) -> Optional[int]:
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return max_value

    # Sinks down a node at the specified index to the appropriate index in the MaxHeap object
    def _sink_down(self, index: int):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)
            if (
                left_index < len(self.heap)
                and self.heap[left_index] > self.heap[max_index]
            ):
                max_index = left_index
            if (
                right_index < len(self.heap)
                and self.heap[right_index] > self.heap[max_index]
            ):
                max_index = right_index
            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                break

    # Swaps the values of two nodes using their specified index in the MaxHeap object
    def _swap(self, index1: int, index2: int):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    # Prints the MaxHeap object
    def display_heap(self):
        if not self.heap:
            print("Empty heap")
        else:
            print(self.heap)

    # Makes the MaxHeap object emtpy
    def make_empty(self):
        self.heap = []

    # Returns the left child node index of a node at a specified index in the MaxHeap object
    @staticmethod
    def _left_child(index: int) -> int:
        return 2 * index + 1

    # Returns the right child node index of a node at a specified index in the MaxHeap object
    @staticmethod
    def _right_child(index: int) -> int:
        return 2 * index + 2

    # Returns the parent node index of a node at a specified index in the MaxHeap object
    @staticmethod
    def _parent(index: int) -> int:
        return (index - 1) // 2


if __name__ == "__main__":
    print("\n----- Test: Instantiates a MaxHeap -----\n")
    my_heap = MaxHeap()
    print("heap:")
    my_heap.display_heap()

    print("\n----- Test: Inserts multiple nodes in a MaxHeap -----\n")
    my_heap.insert(99)
    my_heap.insert(72)
    my_heap.insert(61)
    my_heap.insert(58)
    print("heap:")
    my_heap.display_heap()
    print("")

    print("inserted 100 node")
    my_heap.insert(100)
    print("heap:")
    my_heap.display_heap()
    print("")

    print("inserted 75 node")
    my_heap.insert(75)
    print("heap:")
    my_heap.display_heap()

    print("\n----- Test: Removes the root node in a MaxHeap -----\n")
    my_heap.make_empty()
    my_heap.insert(95)
    my_heap.insert(75)
    my_heap.insert(80)
    my_heap.insert(55)
    my_heap.insert(60)
    my_heap.insert(50)
    my_heap.insert(65)
    print("heap:")
    my_heap.display_heap()
    print("")

    print("removed 95 node")
    my_heap.remove()
    print("heap:")
    my_heap.display_heap()
    print("")

    print("removed 80 node")
    my_heap.remove()
    print("heap:")
    my_heap.display_heap()
