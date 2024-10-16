"""
Give the final output and the remaining elements on the stack
- push(4)
- push(2)
- push(15)
- pop()
- push(27)
- pop()
- pop()
- push(3)
- push(4)
- pop()
- pop()
- pop()
"""

stack = []
removed_elements = []

if __name__ == "__main__":
    stack.append(4)
    stack.append(2)
    stack.append(15)
    # print(stack)
    removed_elements.append(stack.pop())
    # print(stack)
    stack.append(27)
    # print(stack)
    removed_elements.append(stack.pop())
    removed_elements.append(stack.pop())
    # print(stack)
    stack.append(3)
    stack.append(4)
    # print(stack)
    removed_elements.append(stack.pop())
    removed_elements.append(stack.pop())
    removed_elements.append(stack.pop())
    # print(stack)
    # print("")

    print("Output")
    print("Removed elements:", removed_elements)
    print("Remaining elements:", stack)
