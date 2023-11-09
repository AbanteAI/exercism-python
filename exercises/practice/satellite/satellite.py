class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def to_dict(self):
        if self.value is None:
            return {}
        return {
            "v": self.value,
            "l": self.left.to_dict() if self.left else {},
            "r": self.right.to_dict() if self.right else {}
        }

def tree_from_traversals(preorder, inorder):
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")
    
    if len(set(preorder)) != len(preorder) or len(set(inorder)) != len(inorder):
        raise ValueError("traversals must contain unique items")
    
    if sorted(preorder) != sorted(inorder):
        raise ValueError("traversals must have the same elements")
    
    def build_tree(preorder, inorder):
        if not preorder or not inorder:
            return None
        
        root_value = preorder[0]
        root = Node(root_value)
        mid = inorder.index(root_value)
        
        root.left = build_tree(preorder[1:mid+1], inorder[:mid])
        root.right = build_tree(preorder[mid+1:], inorder[mid+1:])
        
        return root
    
    return build_tree(preorder, inorder).to_dict()
