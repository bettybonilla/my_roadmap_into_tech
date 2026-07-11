"""
Give the final output and the remaining elements on the queue
- enqueue(4)
- enqueue(2)
- enqueue(15)
- dequeue()
- enqueue(27)
- dequeue()
- dequeue()
- enqueue(3)
- enqueue(4)
- dequeue()
- dequeue()
- dequeue()
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
    # print(queue)
    # print("")

    print("Output")
    print("Removed elements:", removed_elements)
    print("Remaining elements:", queue)
