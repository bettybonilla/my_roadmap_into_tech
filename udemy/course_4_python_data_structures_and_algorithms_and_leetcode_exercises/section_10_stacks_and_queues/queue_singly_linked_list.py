"""
The below represents a queue using a singly-linked list in code
"""

from typing import Any, Optional


class Node:
    # Initializer AKA constructor
    def __init__(self, value: Any):
        self.value = value
        self.next = None


class Queue:
    # Initializer AKA constructor
    def __init__(self, value: Any):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    # Adds a new node to the last place of the Queue object
    def enqueue(self, value: Any):
        new_node = Node(value)
        # Checks if the Queue is empty
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        # Otherwise, adds the new node to the last place of the Queue
        else:
            # Points the next link of the last node to the new node
            self.last.next = new_node
            # Points the last node to the new node which is now the last node at the end of the Queue
            self.last = new_node
        self.length += 1

    # Removes the first node from the first place of the Queue object
    def dequeue(self) -> Optional[Node]:
        # Checks if the Queue is empty
        if self.length == 0:
            return None
        temp = self.first
        # Accounts for when there is only 1 node in the Queue
        if self.length == 1:
            self.first = None
            self.last = None
        # Accounts for when there are 2 or more nodes in the Queue
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp

    # Prints the value of each node of the Queue object
    def display_queue(self):
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
    print("\n----- Test: Instantiates a Queue -----\n")
    my_queue = Queue(4)

    print("first node value:", my_queue.first.value)
    print("first node next link:", my_queue.first.next)
    print("")

    print("queue:")
    my_queue.display_queue()
    print("queue length:", my_queue.length)

    print("\n----- Test: Enqueues a node to the Queue -----\n")
    my_queue.enqueue(7)
    print("queue:")
    my_queue.display_queue()
    print("queue length:", my_queue.length)

    print("\n----- Test: Enqueues multiple nodes to the Queue -----\n")
    my_queue.enqueue(11)
    my_queue.enqueue(14)
    print("queue:")
    my_queue.display_queue()
    print("queue length:", my_queue.length)

    print("\n----- Test: Dequeues a node from the Queue -----\n")
    print("queue:")
    my_queue.display_queue()
    print("queue length:", my_queue.length)
    print("")
    print("dequeued node:", my_queue.dequeue().value)
    print("")
    print("queue:")
    my_queue.display_queue()
    print("queue length:", my_queue.length)

    print("\n----- Test: Dequeues multiple nodes from the Queue -----\n")
    print("queue:")
    my_queue.display_queue()
    print("queue length:", my_queue.length)
    print("")
    print("dequeued node:", my_queue.dequeue().value)
    print("dequeued node:", my_queue.dequeue().value)
    print("")
    print("queue:")
    my_queue.display_queue()
    print("queue length:", my_queue.length)

    print("\n----- Test: Dequeues an empty Queue -----\n")
    print("queue:")
    my_queue.display_queue()
    print("queue length:", my_queue.length)
    print("")
    print("dequeued node:", my_queue.dequeue().value)
    print("dequeued node:", my_queue.dequeue())
    print("")
    print("queue:")
    my_queue.display_queue()
    print("queue length:", my_queue.length)
