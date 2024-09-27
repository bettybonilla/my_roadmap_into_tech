import unittest
from typing import Optional

from exercise_16_find_kth_node_from_end import LinkedList, find_kth_from_end


class Table:
    def __init__(self, k: int, expected: Optional[int]):
        self.k = k
        self.expected = expected


class Test(unittest.TestCase):
    def test_find_kth_from_end(self):
        my_linked_list = LinkedList(1)
        my_linked_list.append(2)
        my_linked_list.append(3)
        my_linked_list.append(4)
        my_linked_list.append(5)

        cases = [
            Table(2, 4),
            Table(1, 5),
            Table(3, 3),
            Table(4, 2),
            Table(5, None),
            Table(7, None),
        ]

        for i, case in enumerate(cases):
            result = find_kth_from_end(my_linked_list, case.k)
            print(f"Test case: {i + 1}")
            if result:
                self.assertEqual(
                    result.value, case.expected, f"Test case: {i + 1} failed"
                )
            if result is None:
                self.assertEqual(result, case.expected, f"Test case: {i + 1} failed")


if __name__ == "__main__":
    unittest.main()
