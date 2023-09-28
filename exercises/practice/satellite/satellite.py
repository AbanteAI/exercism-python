def tree_from_traversals(preorder, inorder):
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")
def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return {}

    root_value = preorder.pop(0)

    root = {"v": root_value, "l": None, "r": None}

    inorder_index = inorder.index(root_value)
    root["l"] = build_tree(preorder, inorder[:inorder_index])
    root["r"] = build_tree(preorder, inorder[inorder_index + 1:])

    return root