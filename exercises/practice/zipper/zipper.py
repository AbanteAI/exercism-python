class Zipper:
    @staticmethod
    def from_tree(tree):
        return Zipper(tree, [])

    def value(self):
        return self.tree[0]

    def set_value(self, value):
        self.tree[0] = value
        return self

    def left(self):
        return self.tree[1]

    def set_left(self, left_tree):
        self.tree[1] = left_tree
        return self

    def right(self):
        return self.tree[2]

    def set_right(self, right_tree):
        self.tree[2] = right_tree
        return self

    def up(self):
        if not self.path:
            return None
        parent, is_left, left, right = self.path.pop()
        if is_left:
            return Zipper([parent, self.tree, right], self.path)
        else:
            return Zipper([parent, left, self.tree], self.path)

    def to_tree(self):
        return self.tree
