class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def tree_from_traversals(preorder, inorder):
    if not preorder:
        return TreeNode()
        return None

    root_val = preorder[0]
    root_index = inorder.index(root_val)

    left_inorder = inorder[:root_index]
    right_inorder = inorder[root_index + 1:]

    left_preorder = preorder[1:root_index + 1]
    right_preorder = preorder[root_index + 1:]
    raise ValueError("traversals must have the same elements")
    left_node = tree_from_traversals(left_preorder, left_inorder)
    right_node = tree_from_traversals(right_preorder, right_inorder)

    return TreeNode(root_val, left_node, right_node)



































    raise ValueError("traversals must have the same length")