"""
The below represents a queue in code
"""

from typing import Any, NoReturn, Optional


# Creates an empty queue
# To specify an empty list, you would use the NoReturn type hint in your function’s signature
def create_queue() -> list[NoReturn]:
    return []


# Checks if the queue is empty
def is_empty(your_queue: list[Any]) -> bool:
    return len(your_queue) == 0


# Inserts item/element to the end of the queue
def insert_to_end(your_queue: list[Any], item: Any):
    your_queue.append(item)
    print(f"{item} was inserted to the end of the queue")


# Removes item/element at the front of the queue
def remove_from_front(your_queue: list[Any]) -> Optional[Any]:
    if is_empty(your_queue):
        return None
    return your_queue.pop(0)


if __name__ == "__main__":
    queue = create_queue()
    print(queue)
    insert_to_end(queue, 4)
    insert_to_end(queue, 7)
    print(queue)
    print(remove_from_front(queue))
    print(queue)
