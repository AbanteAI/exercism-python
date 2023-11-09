class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = str(data)
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
        data_str = str(data)
        if self.root is None:
            self.root = TreeNode(data_str)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        data_str = str(data)
        if data_str <= node.data:
            if node.left is None:
                node.left = TreeNode(data_str)
            else:
                self._insert_recursive(node.left, data_str)
        else:
            if node.right is None:
                node.right = TreeNode(data_str)
            else:
                self._insert_recursive(node.right, data_str)

    def data(self):
        return self.root

    def sorted_data(self):
        return self._in_order_traversal(self.root)

    def _in_order_traversal(self, node):
        if node is None:
            return []
        return self._in_order_traversal(node.left) + [str(node.data)] + self._in_order_traversal(node.right)
