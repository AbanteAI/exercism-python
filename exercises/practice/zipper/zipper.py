class Zipper:
    def __init__(self, tree, path):
        self.tree = tree
        self.path = path
    @staticmethod
    def from_tree(tree):
        return Zipper(tree, [])

    def value(self):
        return self.tree['value']

    def set_value(self, value):
        self.tree['value'] = value
        return self

    def left(self):
        return Zipper(self.tree['left'], self.path + [{'dir': 'right', 'tree': self.tree['right']}]) if self.tree['left'] else None

    def set_left(self, left_tree):
        self.tree['left'] = left_tree
        return self

    def right(self):
        return Zipper(self.tree['right'], self.path + [{'dir': 'left', 'tree': self.tree['left']}]) if self.tree['right'] else None

    def set_right(self, right_tree):
        self.tree['right'] = right_tree
        return self

    def up(self):
        if not self.path:
            return None

        last = self.path[-1]
        new_path = self.path[:-1]
        new_tree = {'value': last['tree']['value'], last['dir']: self.tree, 'left' if last['dir'] == 'right' else 'right': last['tree']['left' if last['dir'] == 'right' else 'right']}

        return Zipper(new_tree, new_path)

    def to_tree(self):
        return self.tree if not self.path else self.up().to_tree()
