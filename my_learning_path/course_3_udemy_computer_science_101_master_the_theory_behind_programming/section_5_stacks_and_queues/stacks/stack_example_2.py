"""
Give the final output and the remaining elements on the stack
- push(10)
- pop()
- push(2)
- push(5)
- push("C")
- pop()
- pop()
- push(14)
- push("Dog")
- pop()
- pop()
"""

stack = []
removed_elements = []

if __name__ == "__main__":
    stack.append(10)
    # print(stack)
    removed_elements.append(stack.pop())
    # print(stack)
    stack.append(2)
    stack.append(5)
    stack.append("C")
    # print(stack)
    removed_elements.append(stack.pop())
    removed_elements.append(stack.pop())
    # print(stack)
    stack.append(14)
    stack.append("Dog")
    # print(stack)
    removed_elements.append(stack.pop())
    removed_elements.append(stack.pop())
    # print(stack)
    # print("")

    print("Output")
    print("Removed elements:", removed_elements)
    print("Remaining elements:", stack)
