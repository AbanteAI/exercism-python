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

        # Reorient the tree
        self._reorient(node, parent)

        # Update the current tree
        self.label = node.label
        self.children = node.children

    def _find_with_parent(self, label, parent=None):
        if self.label == label:
            return self, None  # No parent for the root node
        for index, child in enumerate(self.children):
            if child.label == label:
                return child, index
            found, parent_index = child._find_with_parent(label)
            if found:
                return found, parent_index
        return None, None

    def _reorient(self, node, parent):
        # Move up the tree, making the current node the parent of its parent
        while parent is not None:
            grandparent, parent_index = self._find_with_parent(parent.label)
            # Remove the current node from its parent's children
            parent.children.pop(parent_index)
            # Add the parent as a child of the current node
            node.children.append(parent)
            # Reorient the grandparent
            node, parent = parent, grandparent

    def path_to(self, from_node, to_node):
        # Reorient the tree to from_node
        self.from_pov(from_node)

        # Find the path to to_node
        path = self._find_path(to_node)
        if path is None:
            raise ValueError(f"No path found from {from_node} to {to_node}")
        return path

    def _find_path(self, label, path=None):
        if path is None:
            path = []
        path.append(self.label)

        if self.label == label:
            return path
        for child in self.children:
            found_path = child._find_path(label, path.copy())
            if found_path:
                return found_path
        return None
