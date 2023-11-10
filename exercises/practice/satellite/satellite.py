def tree_from_traversals(preorder, inorder):
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")
    if sorted(preorder) != sorted(inorder):
        raise ValueError("traversals must have the same elements")
    if len(set(preorder)) != len(preorder) or len(set(inorder)) != len(inorder):
        raise ValueError("traversals must contain unique items")

    def build_tree(preorder, inorder):
        if not preorder or not inorder:
            return {}
        root_value = preorder[0]
        root = TreeNode(root_value)
        root_index = inorder.index(root_value)
        root.left = build_tree(preorder[1:1 + root_index], inorder[:root_index])
        root.right = build_tree(preorder[1 + root_index:], inorder[root_index + 1:])
        return root.to_dict()

    class TreeNode:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def to_dict(self):
            return {
                'v': self.value,
                'l': self.left.to_dict() if self.left else {},
                'r': self.right.to_dict() if self.right else {}
            }

    return build_tree(preorder, inorder)