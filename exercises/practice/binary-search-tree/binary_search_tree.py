class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'


class BinarySearchTree:
    def __init__(self, tree_data):
        self.root = None
        for value in tree_data:
            self.insert(value)
    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            current = self.root
            while True:
                if value <= current.data:
                    if current.left is None:
                        current.left = TreeNode(value)
                        break
                    current = current.left
                else:
                    if current.right is None:
                        current.right = TreeNode(value)
                        break
                    current = current.right

    def data(self):
        return self.root

    def sorted_data(self):
        return list(self.inorder_traversal(self.root))
    def inorder_traversal(self, node):
        if node is None:
            return
        yield from self.inorder_traversal(node.left)
        yield node.data
        yield from self.inorder_traversal(node.right)
