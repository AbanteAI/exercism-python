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
    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(self.root, data)

    def data(self):
        return self.root.data if self.root else None

    def sorted_data(self):
        def _in_order_traversal(node):
            if node is not None:
                yield from _in_order_traversal(node.left)
                yield node.data
                yield from _in_order_traversal(node.right)

        return list(_in_order_traversal(self.root)) if self.root else []

        def _in_order_traversal(node):
            if node is not None:
                yield from _in_order_traversal(node.left)
                yield node.data
                yield from _in_order_traversal(node.right)

        return list(_in_order_traversal(self.root))
