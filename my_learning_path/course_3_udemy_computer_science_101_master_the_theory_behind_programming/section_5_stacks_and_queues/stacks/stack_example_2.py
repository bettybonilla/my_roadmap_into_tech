"""
Give the final output and the remaining elements on the stack
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

stack = []
removed_elements = []

if __name__ == "__main__":
    stack.insert(0, 10)
    # print(stack)
    removed_elements.append(stack.pop(0))
    # print(stack)
    stack.insert(0, 2)
    stack.insert(0, 5)
    stack.insert(0, "C")
    # print(stack)
    removed_elements.append(stack.pop(0))
    removed_elements.append(stack.pop(0))
    # print(stack)
    stack.insert(0, 14)
    stack.insert(0, "Dog")
    # print(stack)
    removed_elements.append(stack.pop(0))
    removed_elements.append(stack.pop(0))
    # print(stack)

    print("Output")
    print("Removed elements:", removed_elements)
    print("Remaining elements:", stack)
