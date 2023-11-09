class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'


class BinarySearchTree:
    def __init__(self, tree_data):
        self.root = None
        for value in tree_data:
            self.insert(value)
    def insert(self, data):
        # Ensure that the data is stored as a string
        data = str(data)
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if data <= node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursive(node.right, data)

    def data(self):
        return self.root

    def sorted_data(self):
        return self._in_order_traversal(self.root)

    def _in_order_traversal(self, node):
        if node is None:
            return []
        else:
            return self._in_order_traversal(node.left) + [node.data] + self._in_order_traversal(node.right)
