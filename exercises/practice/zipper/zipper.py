class Zipper:
    def __init__(self, tree, parent=None):
        self.tree = tree
        self.parent = parent

    @staticmethod
    def from_tree(tree):
        return Zipper(tree)

    def value(self):
        return self.tree["value"]

    def set_value(self, value):
        self.tree["value"] = value
        return self

    def left(self):
        if self.tree["left"]:
            return Zipper(self.tree["left"], self)
        return None

    def set_left(self, left_tree):
        self.tree["left"] = left_tree
        return self

    def right(self):
        if self.tree["right"]:
            return Zipper(self.tree["right"], self)
        return None

    def set_right(self, right_tree):
        self.tree["right"] = right_tree
        return self

    def up(self):
        return self.parent

    def to_tree(self):
        if self.parent:
            return self.parent.to_tree()
        return self.tree
