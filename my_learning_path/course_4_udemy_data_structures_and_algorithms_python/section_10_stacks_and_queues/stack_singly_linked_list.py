"""
The below represents a stack using a singly-linked list in code
"""

from typing import Any, Optional


class Node:
    # Initializer AKA constructor
    def __init__(self, value: Any):
        self.value = value
        self.next = None


class Stack:
    # Initializer AKA constructor
    def __init__(self, value: Any):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    # Adds a new node to the top of the Stack object
    def push(self, value: Any):
        new_node = Node(value)
        # Checks if the Stack is empty
        if self.height == 0:
            self.top = new_node
        # Otherwise, adds the new node to the top of the Stack
        else:
            # Points the next link of the new node to the last node
            new_node.next = self.top
            # Points the top node to the new node which is now the last node at the top of the Stack
            self.top = new_node
        self.height += 1

    # Removes the last node at the top of the Stack object
    def pop(self) -> Optional[Node]:
        # Checks if the Stack is empty
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp

    # Prints the value of each node of the Stack object
    def display_stack(self):
        if self.height == 0:
            print("Empty stack")
        else:
            temp = self.top
            while temp:
                print(temp.value)
                print("↓")
                temp = temp.next
            print("None")


if __name__ == "__main__":
    print("\n----- Test: Instantiates a Stack -----\n")
    my_stack = Stack(4)

    print("top node value:", my_stack.top.value)
    print("top node next link:", my_stack.top.next)
    print("")

    print("stack:")
    my_stack.display_stack()
    print("")
    print("stack height:", my_stack.height)

    print("\n----- Test: Pushes a node to the Stack -----\n")
    my_stack.push(7)
    print("stack:")
    my_stack.display_stack()
    print("")
    print("stack height:", my_stack.height)

    print("\n----- Test: Pushes multiple nodes to the Stack -----\n")
    my_stack.push(11)
    my_stack.push(14)
    print("stack:")
    my_stack.display_stack()
    print("")
    print("stack height:", my_stack.height)

    print("\n----- Test: Pops a node from the Stack -----\n")
    print("stack:")
    my_stack.display_stack()
    print("")
    print("stack height:", my_stack.height)
    print("")
    print("popped node:", my_stack.pop().value)
    print("")
    print("stack:")
    my_stack.display_stack()
    print("")
    print("stack height:", my_stack.height)

    print("\n----- Test: Pops multiple nodes from the Stack -----\n")
    print("stack:")
    my_stack.display_stack()
    print("")
    print("stack height:", my_stack.height)
    print("")
    print("popped node:", my_stack.pop().value)
    print("popped node:", my_stack.pop().value)
    print("")
    print("stack:")
    my_stack.display_stack()
    print("")
    print("stack height:", my_stack.height)

    print("\n----- Test: Pops an empty Stack -----\n")
    print("stack:")
    my_stack.display_stack()
    print("")
    print("stack height:", my_stack.height)
    print("")
    print("popped node:", my_stack.pop().value)
    print("popped node:", my_stack.pop())
    print("")
    print("stack:")
    my_stack.display_stack()
    print("")
    print("stack height:", my_stack.height)
