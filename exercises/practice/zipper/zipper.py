class Zipper:
    @staticmethod
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
        return Zipper(self.focus['left'], self.trail + [(self.focus, 'L')])

    def set_left(self, tree):
        self.focus['left'] = tree
        return self

    def right(self):
        return Zipper(self.focus['right'], self.trail + [(self.focus, 'R')])

    def set_right(self, tree):
        self.focus['right'] = tree
        return self

    def up(self):
        if not self.trail:
            return None
        parent, which = self.trail[-1]
        new_zipper = Zipper(parent, self.trail[:-1])
        if which == 'L':
            new_zipper.focus['left'] = self.focus
        else:
            new_zipper.focus['right'] = self.focus
        return new_zipper
