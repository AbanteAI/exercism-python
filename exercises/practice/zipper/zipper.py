def construct_node(value, left=None, right=None):
    return {'value': value, 'left': left, 'right': right}
class Zipper:
    def __init__(self, focus, path):
        self.focus = focus
        self.path = path
    @staticmethod
    def from_tree(tree):
        # Create a zipper for the binary tree with the focus on the root node
        return Zipper(tree, [])

    def value(self):
        # Return the value of the focus node
        return self.focus['value']

    def set_value(self, value):
        # Set the value of the focus node and return a new zipper
        self.focus['value'] = value
        return self

    def left(self):
        # Move the focus to the left child of the current node
        if self.focus['left']:
            self.path.append(('L', self.focus))
            self.focus = self.focus['left']
            return self
        else:
            return None

    def set_left(self, tree):
        # Set the left child of the focus node and return a new zipper
        self.focus['left'] = tree
        return self

    def right(self):
        # Move the focus to the right child of the current node
        if self.focus['right']:
            self.path.append(('R', self.focus))
            self.focus = self.focus['right']
            return self
        else:
            return None

    def set_right(self, tree):
        # Set the right child of the focus node and return a new zipper
        self.focus['right'] = tree
        return self

    def up(self):
        # Move the focus to the parent node
        if self.path:
            direction, node = self.path.pop()
            if direction == 'L':
                node['left'] = self.focus
            else:
                node['right'] = self.focus
            self.focus = node
            return self
        else:
            return None

    def to_tree(self):
        # Convert the zipper back to a binary tree
        while self.path:
            self.up()
        return self.focus
