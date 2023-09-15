class Zipper:
    def __init__(self, tree, path=None):
        self.tree = tree
        self.path = path or []

    @staticmethod
    def from_tree(tree):
        return Zipper(tree)

    def value(self):
        return self.tree[0]

    def set_value(self, value):
        self.tree[0] = value

    def left(self):
        if len(self.tree) < 2:
            return None
        return Zipper(self.tree[1], self.path + [0])

    def set_left(self, subtree):
        if len(self.tree) < 2:
            return None
        self.tree[1] = subtree

    def right(self):
        if len(self.tree) < 3:
            return None
        return Zipper(self.tree[2], self.path + [1])

    def set_right(self, subtree):
        if len(self.tree) < 3:
            return None
        self.tree[2] = subtree

    def up(self):
        if not self.path:
            return None
        path = self.path[:-1]
        tree = self.tree
        for index in path:
            tree = tree[index]
        return Zipper(tree, path)

    def to_tree(self):
        path = self.path
        tree = self.tree
        for index in path:
            tree = tree[index]
        return tree
    def value(self):
        return self.tree[0]

    def set_value(self, value):
        self.tree[0] = value

    def left(self):
        if len(self.tree) < 2:
            return None
        return Zipper(self.tree[1], self.path + [0])

    def set_left(self, subtree):
        if len(self.tree) < 2:
            return None
        self.tree[1] = subtree

    def right(self):
        if len(self.tree) < 3:
            return None
        return Zipper(self.tree[2], self.path + [1])

    def set_right(self, subtree):
        if len(self.tree) < 3:
            return None
        self.tree[2] = subtree

    def up(self):
        if not self.path:
            return None
        path = self.path[:-1]
        tree = self.tree
        for index in path:
            tree = tree[index]
        return Zipper(tree, path)

    def to_tree(self):
        path = self.path
        tree = self.tree
        for index in path:
            tree = tree[index]
        return tree
