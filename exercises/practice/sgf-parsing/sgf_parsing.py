class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for key, value in self.properties.items():
            if key not in other.properties:
                return False
            if other.properties[key] != value:
                return False
        for key in other.properties.keys():
            if key not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for child, other_child in zip(self.children, other.children):
            if child != other_child:
                return False
        return True

    def __ne__(self, other):
        return not self == other


def parse(input_string):
    if not input_string.startswith("(") or not input_string.endswith(")"):
        raise ValueError("Input does not form a tree")
    if input_string.count("(") != input_string.count(")"):
        raise ValueError("Input does not have proper delimiters")
    if input_string != input_string.upper():
        raise ValueError("Input must be in uppercase")
    if input_string.count(";") == 0:
        raise ValueError("Input does not form a tree with nodes")
    # TODO: Parse the input string and return a tree structure of properties
    return SgfTree()