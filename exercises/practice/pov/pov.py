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
        if self.label == from_node:
            return self

        for child in self.children:
            result = child.from_pov(from_node)
            if result:
                return result

        return None
            return self
    def path_to(self, from_node, to_node):
        from_pov_node = self.from_pov(from_node)
        if from_pov_node:
            return self._find_path(from_pov_node, to_node)

        return None

    def _find_path(self, node, target):
        if node.label == target:
            return [node.label]

        for child in node.children:
            path = self._find_path(child, target)
            if path:
                return [node.label] + path

        return None
            result = child.from_pov(from_node)
            if result:
                return result

        return None

    def path_to(self, from_node, to_node):
        from_pov_node = self.from_pov(from_node)
        if from_pov_node:
            return self._find_path(from_pov_node, to_node)

        return None

    def _find_path(self, node, target):
        if node.label == target:
            return [node.label]

        for child in node.children:
            path = self._find_path(child, target)
            if path:
                return [node.label] + path

        return None
