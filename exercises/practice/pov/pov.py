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
        # Helper function to recursively search for the node and re-parent the tree
        def search_and_reparent(node, parent, new_children):
            if node.label == from_node:
                # Found the node, now re-parent the tree
                return Tree(node.label, new_children)
            for child in node.children:
                # Avoid revisiting the parent node
                if child == parent:
                    continue
                # Attempt to find the node down this subtree
                result = search_and_reparent(child, node, new_children + [node])
                if result:
                    # If the node was found and the result tree is returned,
                    # append the current subtree to the new children and continue
                    new_children.append(Tree(node.label, [c for c in node.children if c != child]))
                    return result
            return None

        # Start the search with an empty list for new children
        new_root = search_and_reparent(self, None, [])
        if new_root is None:
            raise ValueError("Tree could not be reoriented")
        # Replace the current tree's root with the new root
        self.label = new_root.label
        self.children = new_root.children

    def path_to(self, from_node, to_node):
        # Helper function to find the path from the current node to the target node
        def find_path(node, target, path, visited):
            if node.label == target:
                return path + [node.label]
            visited.add(node.label)
            for child in node.children:
                if child.label not in visited:
                    result = find_path(child, target, path + [node.label], visited)
                    if result:
                        return result
            return None

        # Reorient the tree only if necessary
        if self.label != from_node:
            self.from_pov(from_node)
        # Use a set to keep track of visited nodes to prevent infinite recursion
        path = find_path(self, to_node, [], set())
        if path is None:
            raise ValueError("No path found")
        return path
