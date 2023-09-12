class Zipper:
    def __init__(self, value, left, right, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    @staticmethod
    def from_tree(tree):
        if tree is None:
            return None
        return Zipper(tree["value"], tree["left"], tree["right"])

    def value(self):
        return self.value

    def set_value(self, value):
        self.value = value
        return self

    def left(self):
        return self.from_tree(self.left)

    def set_left(self, left):
        self.left = left
        return self

    def right(self):
        return self.from_tree(self.right)

    def set_right(self, right):
        self.right = right
        return self

    def up(self):
        return self.parent

    def to_tree(self):
        return {
            "value": self.value,
            "left": self.left.to_tree() if self.left else None,
            "right": self.right.to_tree() if self.right else None,
        }