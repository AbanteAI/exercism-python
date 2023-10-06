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

    def data(self):
        return self.root

    def sorted_data(self):
        return self.in_order_traversal(self.root)

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value <= node.data:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def in_order_traversal(self, node):
        if node is None:
            return []

        result = []
        result.extend(self.in_order_traversal(node.left))
        result.append(node.data)
        result.extend(self.in_order_traversal(node.right))

        return result
