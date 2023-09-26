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
        if tree_data:
            self.root = TreeNode(tree_data[0])
            for value in tree_data[1:]:
                self.insert(value, self.root)

    def data(self):
        return self.root.data if self.root else None

    def sorted_data(self):
        return self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        if node is None:
            return []
        left_values = self.traverse_in_order(node.left)
        right_values = self.traverse_in_order(node.right)
        return left_values + [node.data] + right_values
