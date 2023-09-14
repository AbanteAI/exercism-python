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
        path = self.path_to(None, from_node)
        if path is None:
            raise ValueError("Tree could not be reoriented")
        return self._reroot(path)

    def _reroot(self, path):
        if len(path) == 1:
            return path[0]
        child = path.pop()
        parent = path.pop()
        parent.children.remove(child)
        child.children.append(parent)
        return self._reroot([child] + path)

    def path_to(self, from_node, to_node):
        if from_node is None:
            return self._path_to(None, [self], to_node)
        return self._path_to(None, self.path_to(None, from_node), to_node)

    def _path_to(self, parent, nodes, to_node):
        if not nodes:
            return None
        node = nodes.pop()
        if node.label == to_node:
            return [node]
        children = node.children[:]
        if parent:
            children.remove(parent)
        path = self._path_to(node, children, to_node)
        if path is not None:
            path.insert(0, node)
            return path
        return self._path_to(parent, nodes, to_node)
