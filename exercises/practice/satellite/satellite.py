def tree_from_traversals(preorder, inorder):
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")
    if set(preorder) != set(inorder):
        raise ValueError("traversals must have the same elements")
    if len(preorder) != len(set(preorder)):
        raise ValueError("traversals must contain unique items")
    
    if not preorder:
        return None
    
    root = preorder[0]
    root_index = inorder.index(root)
    
    left_inorder = inorder[:root_index]
    right_inorder = inorder[root_index + 1:]
    
    left_preorder = preorder[1:1 + len(left_inorder)]
    right_preorder = preorder[1 + len(left_inorder):]
    
    left = tree_from_traversals(left_preorder, left_inorder)
    right = tree_from_traversals(right_preorder, right_inorder)
    
    return (root, left, right)

