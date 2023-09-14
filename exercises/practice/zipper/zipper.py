class Zipper:
    def __init__(self, tree, pointer=None):
        self.tree = tree
        self.pointer = pointer if pointer is not None else tree
    def from_tree(tree):
        return Zipper(tree)

    def value(self):
        return self.pointer["value"]

    def set_value(self, value):
        self.pointer["value"] = value

    def left(self):
        return Zipper(self.tree, self.pointer["left"]) if self.pointer["left"] else None

    def set_left(self, left_tree):
        self.pointer["left"] = left_tree

    def right(self):
        return Zipper(self.tree, self.pointer["right"]) if self.pointer["right"] else None

    def set_right(self, right_tree):
        self.pointer["right"] = right_tree

    def up(self):
        return Zipper(self.tree, self.pointer["parent"]) if "parent" in self.pointer else None

    def to_tree(self):
        return self.tree
