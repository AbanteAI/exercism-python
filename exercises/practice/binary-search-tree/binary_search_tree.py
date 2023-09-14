class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = None
        self.left = None
        self.right = None

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'


class BinarySearchTree:
    def __init__(self, tree_data):
        self.root = None
        for data in tree_data:
    def data(self):
    def data(self):
    def sorted_data(self):
        return self.root
        result = []
        self.in_order_traversal(self.root, result)
        return result

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert_node(self.root, data)

    def _insert_node(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_node(node.left, data)
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_node(node.right, data)

    def in_order_traversal(self, node, result):
        if node:
            self.in_order_traversal(node.left, result)
            result.append(node.data)
            self.in_order_traversal(node.right, result)