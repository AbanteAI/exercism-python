def tree_from_traversals(preorder, inorder):
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def construct_tree(preorder, inorder):
        if not preorder or not inorder:
            return None

        # The first element of preorder is always the root.
        root_value = preorder[0]
        root = Node(root_value)

        # Find the index of the root in inorder list.
        root_index = inorder.index(root_value)

        # Construct left and right subtrees recursively.
        root.left = construct_tree(preorder[1:1 + root_index], inorder[:root_index])
        root.right = construct_tree(preorder[1 + root_index:], inorder[root_index + 1:])

        return root

    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")

    if sorted(preorder) != sorted(inorder):
        raise ValueError("traversals must have the same elements")

    if len(set(preorder)) != len(preorder) or len(set(inorder)) != len(inorder):
        raise ValueError("traversals must contain unique items")

    return construct_tree(preorder, inorder)
