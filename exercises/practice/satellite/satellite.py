def tree_from_traversals(preorder, inorder):
    pass
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def to_dict(self):
        return {
            "v": self.value,
            "l": self.left.to_dict() if self.left else {},
            "r": self.right.to_dict() if self.right else {}
        }

def build_tree(preorder, inorder):
    if len(preorder) != len(inorder):
        raise ValueError("Traversals have different lengths")

    if len(set(preorder)) != len(preorder) or len(set(inorder)) != len(inorder):
        raise ValueError("Traversals have repeated items")
    if not preorder or not inorder:
        return None

    root_value = preorder.pop(0)
    root = TreeNode(root_value)
    index = inorder.index(root_value)

    root.left = build_tree(preorder, inorder[:index])
    root.right = build_tree(preorder, inorder[index + 1:])

    return root

def tree_from_traversals(preorder, inorder):
    return build_tree(preorder, inorder).to_dict()
