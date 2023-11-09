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
        path_to_root = self._find_path_to_root(from_node)
        if path_to_root is None:
            raise ValueError("Tree could not be reoriented")

        # Rebuild the tree from the node's perspective
        new_root = None
        current = None
        for node in reversed(path_to_root):
            if new_root is None:
                new_root = Tree(node.label)
                current = new_root
            else:
                new_child = Tree(node.label)
                node.children.remove(current)
                new_child.children = node.children
                current.children = [new_child]
                current = new_child

        self.label = new_root.label
        self.children = new_root.children

    def _find_path_to_root(self, target_node, current=None, path=None):
        if current is None:
            current = self
            path = []

        if current.label == target_node:
            return path + [current.label]

        for child in current.children:
            found_path = self._find_path_to_root(target_node, child, path + [current.label])
            if found_path:
                return found_path

        return None

    def path_to(self, from_node, to_node):
        # Find paths from the root to the from_node and to_node
        path_from_root_to_from_node = self._find_path_to_root(from_node)
        path_from_root_to_to_node = self._find_path_to_root(to_node)

        if not path_from_root_to_from_node or not path_from_root_to_to_node:
            raise ValueError("No path found")

        # Find the common ancestor to split the paths
        common_ancestor = None
        for from_ancestor, to_ancestor in zip(path_from_root_to_from_node, path_from_root_to_to_node):
            if from_ancestor == to_ancestor:
                common_ancestor = from_ancestor
            else:
                break

        if common_ancestor is None:
            raise ValueError("No path found")

        # Exclude the common ancestor and reverse the path from from_node to common ancestor
        path_from_node_to_common = path_from_root_to_from_node[path_from_root_to_from_node.index(common_ancestor)+1:][::-1]
        path_from_common_to_to_node = path_from_root_to_to_node[path_from_root_to_to_node.index(common_ancestor)+1:]

        # Combine the paths to get the full path from from_node to to_node
        full_path = path_from_node_to_common + [common_ancestor] + path_from_common_to_to_node

        return full_path
