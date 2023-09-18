def tree_from_traversals(preorder, inorder):
    if not preorder and not inorder:
        return {}
        raise ValueError("traversals must have the same length")

    root_value = preorder[0]
    root_index = inorder.index(root_value)
    if set(preorder) != set(inorder):
        raise ValueError("traversals must have the same elements")

    left_inorder = inorder[:root_index]
    right_inorder = inorder[root_index+1:]

    left_preorder = preorder[1:len(left_inorder)+1]
    right_preorder = preorder[len(left_inorder)+1:]

    left_subtree = tree_from_traversals(left_preorder, left_inorder)
    right_subtree = tree_from_traversals(right_preorder, right_inorder)

    return {
        "value": root_value,
        "left": left_subtree,
        "right": right_subtree
    }