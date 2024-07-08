"""
Give the final output and the remaining elements on the queue
- push(4)
- push(2)
- push(15)
- pop(0)
- push(27)
- pop(0)
- pop(0)
- push(3)
- push(4)
- pop(0)
- pop(0)
- pop(0)
"""

queue = []
removed_elements = []

if __name__ == "__main__":
    queue.append(4)
    queue.append(2)
    queue.append(15)
    # print(queue)
    removed_elements.append(queue.pop(0))
    # print(queue)
    queue.append(27)
    # print(queue)
    removed_elements.append(queue.pop(0))
    removed_elements.append(queue.pop(0))
    # print(queue)
    queue.append(3)
    queue.append(4)
    # print(queue)
    removed_elements.append(queue.pop(0))
    removed_elements.append(queue.pop(0))
    removed_elements.append(queue.pop(0))

    print("Output")
    print("Removed elements:", removed_elements)
    print("Remaining elements:", queue)
