"""
You have been tasked with implementing a queue data structure using two stacks in Python, and you need to write the
dequeue method - The dequeue method should remove and return the first element in the queue
- This will use the MyQueue class in the previous coding exercise
"""

from typing import Any, Optional


class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def is_empty(self) -> bool:
        return len(self.stack1) == 0

    def peek(self) -> Any:
        return self.stack1[-1]

    def enqueue(self, value: Any):
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(value)
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())

    # WRITE DEQUEUE METHOD HERE
    def dequeue(self) -> Optional[Any]:
        if self.is_empty():
            return None
        return self.stack1.pop()


if __name__ == "__main__":
    # Create a new queue
    q = MyQueue()

    # Enqueue some values
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    # Output the front of the queue
    print("Front of the queue:", q.peek())

    # Dequeue some values
    print("Dequeued value:", q.dequeue())
    print("Dequeued value:", q.dequeue())

    # Enqueue another value
    q.enqueue(4)

    # Output the front of the queue again
    print("Front of the queue:", q.peek())

    # Dequeue all remaining values
    print("Dequeued value:", q.dequeue())
    print("Dequeued value:", q.dequeue())

    # Check if the queue is empty
    print("Is the queue empty?", q.is_empty())

    # Dequeue from an empty queue and check if it returns None
    print("Dequeued value from empty queue:", q.dequeue())

    """
    EXPECTED OUTPUT:
    ----------------
    Front of the queue: 1
    Dequeued value: 1
    Dequeued value: 2
    Front of the queue: 3
    Dequeued value: 3
    Dequeued value: 4
    Is the queue empty? True
    Dequeued value from empty queue: None
    """
