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
        for item in tree_data:
            self.insert(item)
        pass
    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            node = self.root
            while True:
                if value <= node.data:
                    if node.left is None:
                        node.left = TreeNode(value)
                        break
                    node = node.left
                else:
                    if node.right is None:
                        node.right = TreeNode(value)
                        break
                    node = node.right

    def data(self):
        return self.root

    def sorted_data(self):
        return self.in_order_traversal(self.root)
        pass
    def in_order_traversal(self, node):
        if node is None:
            return []

        left = self.in_order_traversal(node.left)
        right = self.in_order_traversal(node.right)

        return left + [node.data] + right
