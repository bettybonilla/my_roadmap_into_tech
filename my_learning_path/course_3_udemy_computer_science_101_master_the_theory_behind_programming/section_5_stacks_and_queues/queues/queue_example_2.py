"""
Give the final output and the remaining elements on the queue
- enqueue(10)
- dequeue()
- enqueue(2)
- enqueue(5)
- enqueue("C")
- dequeue()
- dequeue()
- enqueue(14)
- enqueue("Dog")
- dequeue()
- dequeue()
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
    # print("")

    print("Output")
    print("Removed elements:", removed_elements)
    print("Remaining elements:", queue)
