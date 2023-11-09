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
    def unescape(value):
        # Handle escape sequences according to SGF specification
        return value.replace('\\\\', '\\').replace('\\]', ']')

    def split_properties(properties_string):
        # Split the properties by closing brackets followed by uppercase letters
        return re.split(r'(?<=\])(?=[A-Z])', properties_string)

    def parse_node(node_string):
        # Extract properties from a node string
        properties = re.findall(r'([A-Z]+)((?:\[.*?[^\\]\])+)', node_string)
        if not properties:
            raise ValueError("tree with no nodes")
        parsed_properties = {}
        for key, values in properties:
            value_list = re.findall(r'\[(.*?[^\\])\]', values)
            parsed_properties[key] = [unescape(value) for value in value_list]
        return parsed_properties

    def parse_tree(tree_string):
        # Parse the tree recursively
        if not tree_string.startswith('(') or not tree_string.endswith(')'):
            raise ValueError("tree missing")
        tree_string = tree_string[1:-1].strip()
        if not tree_string:
            raise ValueError("tree with no nodes")
        subtrees = re.split(r'(?<=\))(?=\()', tree_string)
        nodes = split_properties(subtrees[0])
        root_properties = parse_node(nodes[0])
        children = [parse_tree(subtree) for subtree in subtrees[1:]]
        return SgfTree(root_properties, children)

    input_string = input_string.strip()
    if not input_string:
        raise ValueError("tree missing")
    if any(char.islower() for char in re.findall(r'[A-Za-z]', input_string)):
        raise ValueError("property must be in uppercase")
    return parse_tree(input_string)
