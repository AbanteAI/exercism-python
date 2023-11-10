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
        # Find the node in the tree
        node, parent = self._find_with_parent(from_node)
        if node is None:
            raise ValueError("Tree could not be reoriented")

        # Reorient the tree from the node
        self._reorient(node, parent)
        self.label = node.label
        self.children = node.children
        return self

    def _find_with_parent(self, label, parent=None):
        if self.label == label:
            return self, parent
        for child in self.children:
            result, node_parent = child._find_with_parent(label, self)
            if result is not None:
                return result, node_parent
        return None, None

    def _reorient(self, node, parent):
        if parent is None:
            return
        parent.children.remove(node)
        node.children.append(parent)
        for child in parent.children:
            self._reorient(child, parent)
        self._reorient(parent, self._find_parent(parent.label))

    def _find_parent(self, label):
        for child in self.children:
            if child.label == label:
                return self
            parent = child._find_parent(label)
            if parent is not None:
                return parent
        return None

    def path_to(self, from_node, to_node):
        # Reorient the tree to the from_node
        self.from_pov(from_node)

        # Find the path to the to_node
        path = self._find_path(to_node)
        if path is None:
            raise ValueError("No path found")
        return path

    def _find_path(self, label, path=None):
        if path is None:
            path = []
        path.append(self.label)
        if self.label == label:
            return path
        for child in self.children:
            child_path = child._find_path(label, path.copy())
            if child_path:
                return child_path
        return None
