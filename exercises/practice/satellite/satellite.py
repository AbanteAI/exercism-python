def tree_from_traversals(preorder, inorder):
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")

    if set(preorder) != set(inorder):
        raise ValueError("traversals must have the same elements")

    if len(set(preorder)) != len(preorder):
        raise ValueError("traversals must contain unique items")

    if len(preorder) == 0:
        return {}

    root_value = preorder[0]
    root_index = inorder.index(root_value)

    left_inorder = inorder[:root_index]
    right_inorder = inorder[root_index + 1:]

    left_preorder = [value for value in preorder if value in left_inorder]
    right_preorder = [value for value in preorder if value in right_inorder]

    left_subtree = tree_from_traversals(left_preorder, left_inorder)
    right_subtree = tree_from_traversals(right_preorder, right_inorder)

    return TreeNode(root_value, left_subtree, right_subtree)
