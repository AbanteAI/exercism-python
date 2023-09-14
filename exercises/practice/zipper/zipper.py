class Zipper:
    def __init__(self, node, parent=None):
        self.node = node
        self.parent = parent

    @staticmethod
    def from_tree(tree):
        return Zipper(tree) if tree else None

    def value(self):
        return self.node["value"]

    def set_value(self, value):
        self.node["value"] = value
        return self

    def left(self):
        return Zipper(self.node["left"], self) if self.node["left"] else None

    def set_left(self, left_node):
        self.node["left"] = left_node
        return self

    def right(self):
        return Zipper(self.node["right"], self) if self.node["right"] else None

    def set_right(self, right_node):
        self.node["right"] = right_node
        return self

    def up(self):
        return self.parent

    def to_tree(self):
        return self.node