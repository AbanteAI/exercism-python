class Zipper:
    def __init__(self, focus, ancestors):
        self.focus = focus
        self.ancestors = ancestors

    @staticmethod
    def from_tree(tree):
        return Zipper(tree, [])

    def to_tree(self):
        node = self.focus
        for ancestor in reversed(self.ancestors):
            if ancestor[1] == 'left':
                node = {'value': ancestor[0], 'left': node, 'right': ancestor[2]}
            else:
                node = {'value': ancestor[0], 'left': ancestor[2], 'right': node}
        return node

    def value(self):
        return self.focus['value']

    def set_value(self, value):
        self.focus['value'] = value
        return self

    def left(self):
        if self.focus['left'] is None:
            return None
        return Zipper(self.focus['left'], self.ancestors + [(self.focus['value'], 'left', self.focus['right'])])

    def set_left(self, tree):
        self.focus['left'] = tree
        return self

    def right(self):
        if self.focus['right'] is None:
            return None
        return Zipper(self.focus['right'], self.ancestors + [(self.focus['value'], 'right', self.focus['left'])])

    def set_right(self, tree):
        self.focus['right'] = tree
        return self

    def up(self):
        if not self.ancestors:
            return None
        parent_value, parent_side, sibling = self.ancestors.pop()
        parent = {'value': parent_value, parent_side: self.focus, 'left' if parent_side == 'right' else 'right': sibling}
        return Zipper(parent, self.ancestors)

    # Additional methods `prev`, `next`, `insert_before`, `insert_after`, and `delete` would be implemented here.
    # Their implementation will depend on the specific requirements and the structure of the binary tree.
