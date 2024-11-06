"""
Implement the dequeue method for the Queue class that removes the first node from the queue and returns it
- The method should perform the following tasks:
    1. If the queue is empty (i.e., the length is 0), return None
    2. Store a reference to the current first node in a temporary variable, temp
    3. If the queue has only one node (i.e., the length is 1), set both the first and last attributes of the Queue class
    to None
    4. If the queue has more than one node, perform the following steps:
        - Update the first attribute of the Queue class to point to the next node in the queue
        - Set the next attribute of the removed node (stored in the temporary variable) to None
    5. Decrement the length attribute of the Queue class by 1
    6. Return the removed node (stored in the temporary variable)
"""

from typing import Any, Optional


class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value: Any):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def enqueue(self, value: Any):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self) -> Optional[Node]:
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp

    def print_queue(self):
        if self.length == 0:
            print("Empty queue")
        else:
            values = []
            temp = self.first
            while temp:
                values.append(str(temp.value))
                temp = temp.next
            values.append("None")
            print(" -> ".join(values))


if __name__ == "__main__":
    my_queue = Queue(1)
    my_queue.enqueue(2)

    # (2) Items - Returns 1 Node
    print(my_queue.dequeue().value)
    # (1) Item -  Returns 2 Node
    print(my_queue.dequeue().value)
    # (0) Items - Returns None
    print(my_queue.dequeue())

    """
    EXPECTED OUTPUT:
    ----------------
    1
    2
    None
    """
