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
        path = self.path_to(self.label, from_node)
        if path is None:
            raise ValueError("Tree could not be reoriented")

        new_tree = self._reroot(path)
        return new_tree

    def path_to(self, from_node, to_node):
        def _path_to(node, target, visited):
            if node is None or node.label in visited:
                return None
            visited.add(node.label)
            if node.label == target:
                return [node.label]
            for child in node.children:
                path = _path_to(child, target, visited)
                if path is not None:
                    path.insert(0, node.label)
                    return path
            return None

        return _path_to(self, from_node, set()) + _path_to(self, to_node, set())[1:]

    def _reroot(self, path):
        if len(path) == 1:
            return Tree(path[0])

        new_tree = Tree(path[0], [Tree(path[1])])
        current = new_tree.children[0]
        for i in range(2, len(path)):
            current.children.append(Tree(path[i]))
            current = current.children[-1]

        def _reroot_children(node, parent_label):
            if node is None:
                return
            new_children = [c for c in node.children if c.label != parent_label]
            for child in new_children:
                _reroot_children(child, node.label)
            node.children = new_children

        _reroot_children(self, path[-1])
        return new_tree
