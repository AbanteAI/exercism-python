import re
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


def _parse_properties(properties_str):
    properties = {}
    for prop in re.findall(r"([A-Z]+)\[([^\]]*?)]", properties_str):
        key, value = prop
        if key in properties:
            properties[key].append(value)
        else:
            properties[key] = [value]
    return properties

def _parse_children(children_str):
    children = []
    while children_str:
        child, children_str = _parse_tree(children_str)
        children.append(child)
    return children

def _parse_tree(tree_str):
    if not tree_str.startswith("("):
        raise ValueError("tree missing")
    tree_str = tree_str[1:]
    if not tree_str.startswith(";"):
        raise ValueError("tree with no nodes")
    tree_str = tree_str[1:]
    properties_str, _, children_str = re.split(r"[\(\)]", tree_str, maxsplit=2)
    properties = _parse_properties(properties_str)
    children = _parse_children(children_str)
    return SgfTree(properties, children), children_str

def parse(input_string):
    tree, remaining = _parse_tree(input_string)
    if remaining:
        raise ValueError("extra data")
    return tree
def parse(input_string):
    pass
