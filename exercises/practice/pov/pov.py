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
        if from_node not in self.__dict__():
            raise ValueError("Invalid from_node")
        new_tree = Tree(from_node)
        self._reorient(self, from_node, new_tree)
        return new_tree

        for child in node.children:
            if child.label == from_node:
                new_tree.children.extend(child.children)
            else:
                self._reorient(child, from_node, new_tree)

    def path_to(self, from_node, to_node):
        pass



    def path_to(self, from_node, to_node):
        pass
