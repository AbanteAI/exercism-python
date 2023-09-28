def tree_from_traversals(preorder, inorder):
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")
    if set(preorder) != set(inorder):
        raise ValueError("traversals must have the same elements")
    if len(set(preorder)) != len(preorder):
        raise ValueError("traversals must contain unique items")
    # TODO: Implement tree reconstruction logic
    # Tree reconstruction logic
    if not preorder:
        return {}
    
    root_value = preorder[0]
    root_index = inorder.index(root_value)
    
    left_preorder = preorder[1:root_index+1]
    left_inorder = inorder[:root_index]
    right_preorder = preorder[root_index+1:]
    right_inorder = inorder[root_index+1:]
    
    return {
        "v": root_value,
        "l": tree_from_traversals(left_preorder, left_inorder),
        "r": tree_from_traversals(right_preorder, right_inorder)
    }