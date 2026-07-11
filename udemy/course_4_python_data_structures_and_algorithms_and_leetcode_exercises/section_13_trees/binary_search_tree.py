"""
The below represents a binary search tree (BST) in code
"""


class Node:
    # Initializer AKA constructor
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    # Initializer AKA constructor
    def __init__(self):
        self.root = None

    # Searches for a node in the BinarySearchTree object
    def contains(self, value: int) -> bool:
        temp = self.root
        while temp:
            # Checks the nodes to the left of (less than) the root node in the BinarySearchTree
            if value < temp.value:
                temp = temp.left
            # Checks the nodes to the right of (greater than) the root node in the BinarySearchTree
            elif value > temp.value:
                temp = temp.right
            # Otherwise, value is equal to the node and therefore it is in the BinarySearchTree
            else:
                return True
        return False

    # Inserts a new node in the BinarySearchTree object
    def insert(self, value: int) -> bool:
        new_node = Node(value)
        # Checks if the BinarySearchTree is empty
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            # Checks if the new node is already in the BinarySearchTree since duplicate values are not allowed
            if new_node.value == temp.value:
                return False
            # Otherwise, inserts the new node in the BinarySearchTree
            # If the new node is less than the root node, inserts the new node to the left of the root node in the
            # BinarySearchTree
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            # If the new node is greater than the root node, inserts the new node to the right of the root node in the
            # BinarySearchTree
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right


if __name__ == "__main__":
    print("\n----- Test: Instantiates an empty BinarySearchTree -----\n")
    my_tree = BinarySearchTree()
    print("root node value:", my_tree.root)

    print("\n----- Test: Inserts a node in an empty BinarySearchTree -----\n")
    my_tree.insert(47)
    print("root node value:", my_tree.root.value)

    print("\n----- Test: Inserts multiple nodes in a BinarySearchTree -----\n")
    my_tree.insert(21)
    my_tree.insert(76)
    print("root node value:", my_tree.root.value)
    print("left node value:", my_tree.root.left.value)
    print("right node value:", my_tree.root.right.value)

    print("\n----- Test: Inserts a duplicate node in a BinarySearchTree -----\n")
    print("inserted node:", my_tree.insert(21))

    print("\n----- Test: Searches for a node in a BinarySearchTree -----\n")
    my_tree.insert(18)
    my_tree.insert(27)
    my_tree.insert(52)
    my_tree.insert(82)
    print("contains node:", my_tree.contains(27))
    print("contains node:", my_tree.contains(17))
