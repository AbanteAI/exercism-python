def tree_from_traversals(preorder, inorder):
    if len(preorder) == 0:
        return {}

    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")

    if sorted(preorder) != sorted(inorder):
        raise ValueError("traversals must have the same elements")

    if len(set(preorder)) != len(preorder) or len(set(inorder)) != len(inorder):
        raise ValueError("traversals must contain unique items")

    root = preorder[0]
    root_index = inorder.index(root)

    left_inorder = inorder[:root_index]
    right_inorder = inorder[root_index + 1:]

    left_preorder = preorder[1:1 + len(left_inorder)]
    right_preorder = preorder[1 + len(left_inorder):]

    return {
        "v": root,
        "l": tree_from_traversals(left_preorder, left_inorder),
        "r": tree_from_traversals(right_preorder, right_inorder)
    }