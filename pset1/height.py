# Problem 3: Given the root node of node of a tree, return the height of a tree.
# binary tree

class TreeNode:
    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right = None

def height(root) -> int:
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))