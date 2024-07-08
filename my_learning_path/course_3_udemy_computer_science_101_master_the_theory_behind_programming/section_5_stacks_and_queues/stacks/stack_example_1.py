"""
Give the final output and the remaining elements on the stack
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

stack = []
removed_elements = []

if __name__ == "__main__":
    stack.insert(0, 4)
    stack.insert(0, 2)
    stack.insert(0, 15)
    # print(stack)
    removed_elements.append(stack.pop(0))
    # print(stack)
    stack.insert(0, 27)
    # print(stack)
    removed_elements.append(stack.pop(0))
    removed_elements.append(stack.pop(0))
    # print(stack)
    stack.insert(0, 3)
    stack.insert(0, 4)
    # print(stack)
    removed_elements.append(stack.pop(0))
    removed_elements.append(stack.pop(0))
    removed_elements.append(stack.pop(0))

    print("Output")
    print("Removed elements:", removed_elements)
    print("Remaining elements:", stack)
