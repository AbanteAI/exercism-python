class Zipper:
    def __init__(self, tree, trail=[]):
        self.focus = tree
        self.trail = trail

    @staticmethod
    def from_tree(tree):
        return Zipper(tree)

    def to_tree(self):
        if self.trail:
            return self.up().to_tree()
        return self.focus

    def value(self):
        return self.focus['value']

    def set_value(self, value):
        self.focus['value'] = value
        return self

    def left(self):
        if self.focus['left']:
            return Zipper(self.focus['left'], self.trail + [{'direction': 'left', 'node': self.focus}])
        return None

    def set_left(self, tree):
        self.focus['left'] = tree
        return self

    def right(self):
        if self.focus['right']:
            return Zipper(self.focus['right'], self.trail + [{'direction': 'right', 'node': self.focus}])
        return None

    def set_right(self, tree):
        self.focus['right'] = tree
        return self

    def up(self):
        if not self.trail:
            return None
        parent_info = self.trail.pop()
        direction = parent_info['direction']
        parent = parent_info['node']
        if direction == 'left':
            parent['left'] = self.focus
        else:
            parent['right'] = self.focus
        return Zipper(parent, self.trail)
