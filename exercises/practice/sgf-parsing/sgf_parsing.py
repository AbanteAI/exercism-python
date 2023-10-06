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


import re

def parse(input_string):
def parse_node(node_str):
    properties = {}
    children = []

    key_values = re.findall(r'([A-Za-z]+)\[([^\]]*)\]', node_str)
    for key, value in key_values:
        if not key.isupper():
            raise ValueError("property must be in uppercase")
        value = value.replace("\\\\", "\\").replace("\\]", "]").replace("\\\n", "").replace("\\\r", "").replace("\\\t", "")
        if key not in properties:
            properties[key] = [value]
        else:
            properties[key].append(value)

    child_nodes = re.findall(r'\(([^)]+)\)', node_str)
    for child in child_nodes:
        children.append(parse_node(child))

    return SgfTree(properties, children)

if not input_string.startswith('(') or not input_string.endswith(')'):
    raise ValueError("tree missing")

node_str = input_string[1:-1]
if not node_str.startswith(';'):
    raise ValueError("tree with no nodes")

return parse_node(node_str)