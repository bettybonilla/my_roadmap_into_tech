"""
Create a BinarySearchTree class
- The BinarySearchTree class should contain the following components:
    1. A Node class, which serves as the building block for the binary search tree - The Node class should have an
    __init__ method that initializes the following attributes:
        - value: The value of the node
        - left: A reference to the left child node, initialized to None
        - right: A reference to the right child node, initialized to None
    2. The BinarySearchTree class should have an __init__ method that initializes an empty binary search tree - The
    __init__ method should perform the following task:
        - Set the root attribute of the BinarySearchTree class to None, indicating that the tree is initially empty
"""


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None


if __name__ == "__main__":
    my_tree = BinarySearchTree()
    print("Root:", my_tree.root)
