"""
The below represents a binary search tree in code
"""


# Create a node
class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


# Insert a node
def insert(node: Node | None, value: int) -> Node:
    # Base case (exit condition)
    # Returns a new node if node argument is None (Ex: If the tree is empty or if node.left or node.right is None)
    if node is None:
        return Node(value)
    # Recursive case
    # Traverse to the correct position in the tree to insert the node
    else:
        if value < node.value:
            node.left = insert(node.left, value)
        if value > node.value:
            node.right = insert(node.right, value)

    # Returns the updated node in the tree after insertion of new node or returns node passed if a duplicate value is
    # passed therefore, it will not be inserted in the tree - Only unique values are inserted in the tree
    return node


# First, visit all the nodes in the left subtree
# Then, visit the root node
# Last, visit all the nodes in the right subtree
def inorder_traversal(root: Node):
    if root:
        # Traverse left subtree
        inorder_traversal(root.left)

        # Traverse root node
        print(f"{root.value} -> ", end="")

        # Traverse right subtree
        inorder_traversal(root.right)


if __name__ == "__main__":
    root_node = None
    root_node = insert(root_node, 50)
    root_node = insert(root_node, 17)
    root_node = insert(root_node, 72)
    root_node = insert(root_node, 12)
    root_node = insert(root_node, 23)
    root_node = insert(root_node, 54)
    root_node = insert(root_node, 76)
    print("Inorder traversal")
    inorder_traversal(root_node)
