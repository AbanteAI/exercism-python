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
        if from_node == self.label:
            return
        for child in self.children:
            try:
                child.from_pov(from_node)
                # If from_node is found, reorient the tree
                self.children.remove(child)
                child.children.append(Tree(self.label, self.children))
                self.label = child.label
                self.children = child.children
                return
            except ValueError:
                continue
        raise ValueError("Tree could not be reoriented")

    def path_to(self, from_node, to_node):
        if from_node == to_node:
            return [from_node]
        path = [self.label]
        for child in self.children:
            try:
                subpath = child.path_to(from_node, to_node)
                if subpath[0] == from_node or subpath[-1] == to_node:
                    return path + subpath
            except ValueError:
                continue
        raise ValueError("No path found")
