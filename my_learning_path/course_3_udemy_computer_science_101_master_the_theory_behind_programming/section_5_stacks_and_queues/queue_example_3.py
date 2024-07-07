"""
Give the final output and the remaining elements on the queue
- enqueue(10)
- enqueue(15)
- enqueue(17)
- dequeue()
- enqueue("L")
- dequeue()
- dequeue()
- enqueue(14)
- dequeue()
- dequeue()
- enqueue(4)
- dequeue()
"""

queue = []
removed_elements = []

if __name__ == "__main__":
    queue.append(10)
    queue.append(15)
    queue.append(17)
    # print(queue)
    removed_elements.append(queue.pop(0))
    # print(queue)
    queue.append("L")
    # print(queue)
    removed_elements.append(queue.pop(0))
    removed_elements.append(queue.pop(0))
    # print(queue)
    queue.append(14)
    # print(queue)
    removed_elements.append(queue.pop(0))
    removed_elements.append(queue.pop(0))
    # print(queue)
    queue.append(4)
    # print(queue)
    removed_elements.append(queue.pop(0))
    # print(queue)

    print("Output")
    print("Removed elements:", removed_elements)
    print("Remaining elements:", queue)
