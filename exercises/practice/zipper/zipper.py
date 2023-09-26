class Zipper:
    def __init__(self, tree, parent=None, left=None, right=None):
        self.tree = tree
        self.parent = parent
        self.left = left
        self.right = right
    @staticmethod
    def from_tree(tree):
        return Zipper(tree)
    def value(self):
        return self.tree["value"]
    def set_value(self, value):
        self.tree["value"] = value
        return self
        pass

    def left(self):
    def left(self):
        if not self.tree["left"]:
            return None
        return Zipper.from_tree(self.tree["left"]).set_parent(self).set_left(None).set_right(None)
    def set_left(self, left):
        if left:

        if not self.tree[2]:
            return None
        return Zipper(self.tree[2], parent=self, left=None, right=None)
    def set_right(self, right):
        self.tree[2] = right.tree if right else None
        return self
    def set_right(self):
        pass

    def up(self):
        if not self.parent:
            return None
        return Zipper(self.parent.tree, parent=self.parent.parent, left=self.parent.left, right=self.parent.right)

    def to_tree(self):
        return self.tree
