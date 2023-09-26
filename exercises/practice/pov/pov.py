from json import dumps


class Tree:
    def __init__(self, label, children=None):
        self.label = label
        self.children = children if children is not None else []

    def __dict__(self):
        return {self.label: [c.__dict__() for c in sorted(self.children)]}

    def __str__(self, indent=None):
        return dumps(self.__dict__(), indent=indent)

    def __lt__(self, other):
        return self.label < other.label

    def __eq__(self, other):
        return self.__dict__() == other.__dict__()

    def from_pov(self, from_node):
    def from_pov(self, from_node):
        new_tree = self.__class__(from_node)
        new_tree.children = [c.from_pov(from_node) for c in self.children]
        return new_tree
        pass

    def path_to(self, from_node, to_node):
    def path_to(self, from_node, to_node):
        if self.label == from_node:
            return [self.label] + self._path_to(to_node)
        for child in self.children:
            path = child.path_to(from_node, to_node)
            if path:
                return [self.label] + path
        return None

    def _path_to(self, to_node):
        if self.label == to_node:
            return [self.label]
        for child in self.children:
            path = child._path_to(to_node)
            if path:
                return [self.label] + path
        return None
        pass
