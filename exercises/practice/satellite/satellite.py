class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def tree_from_traversals(preorder, inorder):
    if not preorder or not inorder:
        return None
    
    root_val = preorder[0]
    root = TreeNode(root_val)
    
    root_index_inorder = inorder.index(root_val)
    
    left_inorder = inorder[:root_index_inorder]
    right_inorder = inorder[root_index_inorder + 1:]
    
    left_preorder = preorder[1:1 + len(left_inorder)]
    right_preorder = preorder[1 + len(left_inorder):]
    
    root.left = tree_from_traversals(left_preorder, left_inorder)
    root.right = tree_from_traversals(right_preorder, right_inorder)
    
    return root