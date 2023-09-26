class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        return None

        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'

class BinarySearchTree:
    def __init__(self, tree_data):
        if tree_data:
            self.data = tree_data[0]
            self.left = BinarySearchTree([x for x in tree_data[1:] if x <= self.data])
            self.right = BinarySearchTree([x for x in tree_data[1:] if x > self.data])
        else:
            self.data = None
            self.left = None
            self.right = None
        return None
            self.left = BinarySearchTree([x for x in tree_data[1:] if x <= self.data])
            self.right = BinarySearchTree([x for x in tree_data[1:] if x > self.data])
        else:
            self.data = None
            self.left = None
            self.right = None

        return self.data
        return self._traverse_in_order()
        result = []
        if self.left:
            result.extend(self.left._traverse_in_order())
        result.append(self.data)
        if self.right:
            result.extend(self.right._traverse_in_order())
        return result
