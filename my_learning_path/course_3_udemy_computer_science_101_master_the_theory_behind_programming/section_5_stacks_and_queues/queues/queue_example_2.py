"""
Give the final output and the remaining elements on the queue
- push(10)
- pop(0)
- push(2)
- push(5)
- push("C")
- pop(0)
- pop(0)
- push(14)
- push("Dog")
- pop(0)
- pop(0)
"""

queue = []
removed_elements = []

if __name__ == "__main__":
    queue.append(10)
    # print(queue)
    removed_elements.append(queue.pop(0))
    # print(queue)
    queue.append(2)
    queue.append(5)
    queue.append("C")
    # print(queue)
    removed_elements.append(queue.pop(0))
    removed_elements.append(queue.pop(0))
    # print(queue)
    queue.append(14)
    queue.append("Dog")
    # print(queue)
    removed_elements.append(queue.pop(0))
    removed_elements.append(queue.pop(0))
    # print(queue)

    print("Output")
    print("Removed elements:", removed_elements)
    print("Remaining elements:", queue)
