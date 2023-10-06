class Zipper:
    @staticmethod
    def __init__(self, tree, path=None):
        self.tree = tree
        self.path = path or []

        return self.tree[0]

        new_tree = list(self.tree)
        new_tree[0] = value
        return Zipper(new_tree, self.path)

        if not self.tree[1]:
            return None
        return Zipper(self.tree[1][0], self.path + [(0, self.tree[0], self.tree[2])])

        if not self.tree[1]:
            return None
        new_tree = list(self.tree)
        new_tree[1] = [tree] + self.tree[1][1:]
        return Zipper(new_tree, self.path)

        if not self.tree[2]:
            return None
        return Zipper(self.tree[2][0], self.path + [(2, self.tree[0], self.tree[1])])

        if not self.tree[2]:
            return None
        new_tree = list(self.tree)
        new_tree[2] = [tree] + self.tree[2][1:]
        return Zipper(new_tree, self.path)

        if not self.path:
            return None
        direction, parent_value, siblings = self.path[-1]
        if direction == 0:
            return Zipper([parent_value, tree, siblings], self.path[:-1])
        elif direction == 2:
            return Zipper([parent_value, siblings, tree], self.path[:-1])

        return self.tree
