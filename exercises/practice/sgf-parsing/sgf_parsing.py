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
    if not input_string.startswith('(') or not input_string.endswith(')'):
        raise ValueError("tree missing")

    input_string = input_string[1:-1].strip()

    if not input_string.startswith(';'):
        raise ValueError("tree with no nodes")

    input_string = input_string[1:]

    properties_pattern = re.compile(r'([A-Za-z]+)\[((?:\\\\|\\\]|[^]])+)\]')
    properties = {}
    children = []

    while input_string:
        match = properties_pattern.match(input_string)
        if not match:
            raise ValueError("properties without delimiter")

        key, value = match.groups()

        if not key.isupper():
            raise ValueError("property must be in uppercase")

        if key not in properties:
            properties[key] = []

        value = value.replace('\\\n', '').replace('\\]', ']').replace('\\\\', '\\').replace('\n', '\\n').replace('  ', ' ')
        properties[key].append(value)
        input_string = input_string[match.end():].strip()

    return SgfTree(properties, children)