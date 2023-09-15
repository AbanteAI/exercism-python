from json import dumps


class Tree:
    def __init__(self, label, children=None):
        self.label = label
        self.children = children if children is not None else []

    def __dict__(self):
    return {self.label: [c.__dict__() for c in self.children]}

    def __str__(self, indent=None):
        return dumps(self.__dict__(), indent=indent)

    def __lt__(self, other):
        return self.label < other.label

    def __eq__(self, other):
        return self.__dict__() == other.__dict__()

    def from_pov(self, from_node):
        if self.label == from_node:
            return self
        for child in self.children:
            new_root = child.from_pov(from_node)
            if new_root:
                if new_root in child.children:
                    child.children.remove(new_root)
                new_root.children.append(child)
                return new_root
        return None

    def path_to(self, from_node, to_node):
        def find_path(tree, target, path=None):
            if path is None:
                path = []
            if tree is None:
                return None
            if tree.label == target:
                return path + [tree.label]
            for child in tree.children:
                result = find_path(child, target, path + [tree.label])
                if result:
                    return result
            return None

        reoriented_tree = self.from_pov(from_node)
        return find_path(reoriented_tree, to_node)
