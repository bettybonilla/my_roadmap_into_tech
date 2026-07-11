"""
Implement the partition_list member function for the LinkedList class, which partitions the linked list such that all
nodes with values less than x come before nodes with values greater than or equal to x
- NOTE: This linked list class does NOT have a tail which will make this method easier to implement
- The original relative order of the nodes should be preserved
- The function partition_list takes an integer x as a parameter and modifies the current linked list in place according
to the specified criteria - If the linked list is empty (Ex: head is null), the function should return immediately
without making any changes
    - While traversing the linked list, maintain two separate chains: one for values less than x and one for values
    greater than or equal to x
    - Use dummy nodes to simplify the handling of the heads of these chains
    - After processing the entire linked list, connect the two chains to get the desired arrangement
- Example 1:
    - Input:
        - Linked List: 3 -> 8 -> 5 -> 10 -> 2 -> 1
        - x = 5
    - Process:
        - Values less than 5: 3, 2, 1
        - Values greater than or equal to 5: 8, 5, 10
    - Output:
        - Linked List: 3 -> 2 -> 1 -> 8 -> 5 -> 10
- Example 2:
    - Input:
        - Linked List: 1 -> 4 -> 3 -> 2 -> 5 -> 2
        - x = 3
    - Process:
        - Values less than 3: 1, 2, 2
        - Values greater than or equal to 3: 4, 3, 5
    - Output:
        - Linked List: 1 -> 2 -> 2 -> 4 -> 3 -> 5
- NOTE: The solution must maintain the relative order of nodes - For instance, in the first example, even though 8
appears before 5 in the original linked list, the partitioned list must still have 8 before 5 as their relative order
remains unchanged
    - You must solve the problem WITHOUT MODIFYING THE VALUES in the linked list's nodes (Ex: Only the nodes' next
    pointers may be changed)
"""

from typing import Any, Optional, Self


class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value: Any):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value: Any):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1

    def partition_list(self, x: int) -> Optional[Self]:
        if self.head is None:
            return Self
        list1 = []
        list2 = []
        temp = self.head
        for _ in range(self.length):
            if temp.value < x:
                list1.append(temp.value)
            if temp.value >= x:
                list2.append(temp.value)
            temp = temp.next
        self.make_empty()
        for i in list1:
            self.append(i)
        for i in list2:
            self.append(i)

    def print_list(self):
        values = []
        current_node = self.head
        while current_node:
            values.append(str(current_node.value))
            current_node = current_node.next
        values.append("None")
        print(" -> ".join(values))

    def make_empty(self):
        self.head = None
        self.length = 0


if __name__ == "__main__":
    # Function to convert linked list to Python list
    def linkedlist_to_list(head):
        result = []
        current = head
        while current:
            result.append(current.value)
            current = current.next
        return result

    # Function to test partition_list
    def test_partition_list():
        test_cases_passed = 0

        print("-----------------------")

        # Test 1: Normal Case
        print("Test 1: Normal Case")
        x = 3
        print(f"x = {x}")
        ll = LinkedList(3)
        ll.append(1)
        ll.append(4)
        ll.append(2)
        ll.append(5)
        print("Before:", linkedlist_to_list(ll.head))
        ll.partition_list(x)
        print("After:", linkedlist_to_list(ll.head))
        if linkedlist_to_list(ll.head) == [1, 2, 3, 4, 5]:
            print("PASS")
            test_cases_passed += 1
        else:
            print("FAIL")

        print("-----------------------")

        # Test 2: All Equal Values
        print("Test 2: All Equal Values")
        x = 3
        print(f"x = {x}")
        ll = LinkedList(3)
        ll.append(3)
        ll.append(3)
        print("Before:", linkedlist_to_list(ll.head))
        ll.partition_list(x)
        print("After:", linkedlist_to_list(ll.head))
        if linkedlist_to_list(ll.head) == [3, 3, 3]:
            print("PASS")
            test_cases_passed += 1
        else:
            print("FAIL")

        print("-----------------------")

        # Test 3: Single Element
        print("Test 3: Single Element")
        x = 3
        print(f"x = {x}")
        ll = LinkedList(1)
        print("Before:", linkedlist_to_list(ll.head))
        ll.partition_list(x)
        print("After:", linkedlist_to_list(ll.head))
        if linkedlist_to_list(ll.head) == [1]:
            print("PASS")
            test_cases_passed += 1
        else:
            print("FAIL")

        print("-----------------------")

        # Test 4: Already Sorted
        print("Test 4: Already Sorted")
        x = 2
        print(f"x = {x}")
        ll = LinkedList(1)
        ll.append(2)
        ll.append(3)
        print("Before:", linkedlist_to_list(ll.head))
        ll.partition_list(x)
        print("After:", linkedlist_to_list(ll.head))
        if linkedlist_to_list(ll.head) == [1, 2, 3]:
            print("PASS")
            test_cases_passed += 1
        else:
            print("FAIL")

        print("-----------------------")

        # Test 5: Reverse Sorted
        print("Test 5: Reverse Sorted")
        x = 2
        print(f"x = {x}")
        ll = LinkedList(3)
        ll.append(2)
        ll.append(1)
        print("Before:", linkedlist_to_list(ll.head))
        ll.partition_list(x)
        print("After:", linkedlist_to_list(ll.head))
        if linkedlist_to_list(ll.head) == [1, 3, 2]:
            print("PASS")
            test_cases_passed += 1
        else:
            print("FAIL")

        print("-----------------------")

        # Test 6: All Smaller Values
        print("Test 6: All Smaller Values")
        x = 2
        print(f"x = {x}")
        ll = LinkedList(1)
        ll.append(1)
        ll.append(1)
        print("Before:", linkedlist_to_list(ll.head))
        ll.partition_list(x)
        print("After:", linkedlist_to_list(ll.head))
        if linkedlist_to_list(ll.head) == [1, 1, 1]:
            print("PASS")
            test_cases_passed += 1
        else:
            print("FAIL")

        print("-----------------------")

        # Test 7: Single Element, Equal to Partition
        print("Test 7: Single Element, Equal to Partition")
        x = 3
        print(f"x = {x}")
        ll = LinkedList(3)
        print("Before:", linkedlist_to_list(ll.head))
        ll.partition_list(x)
        print("After:", linkedlist_to_list(ll.head))
        if linkedlist_to_list(ll.head) == [3]:
            print("PASS")
            test_cases_passed += 1
        else:
            print("FAIL")

        print("-----------------------")

        # Summary
        print(f"{test_cases_passed} out of 7 tests passed.")

    # Run the test function
    test_partition_list()
