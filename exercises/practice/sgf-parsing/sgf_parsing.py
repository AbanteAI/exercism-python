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
            raise ValueError("input does not form a tree")
        input_string = input_string[1:-1]
        return parse_tree(input_string)

def parse_tree(input_string):
    properties = {}
    children = []
    while input_string:
        if input_string[0] == ";":
            node, input_string = parse_node(input_string[1:])
            children.append(node)
        else:
            key, input_string = parse_property(input_string)
            properties.setdefault(key, []).append(input_string)
    return SgfTree(properties, children)

def parse_node(input_string):
    properties = {}
    while input_string and input_string[0] != ";":
        key, input_string = parse_property(input_string)
        properties.setdefault(key, []).append(input_string)
    return SgfTree(properties), input_string

def parse_property(input_string):
    if not input_string[0].isalpha():
        raise ValueError("property must start with an alphabetic character")
    key = ""
    while input_string and input_string[0].isalpha():
        key += input_string[0]
        input_string = input_string[1:]
    if input_string[0] != "[":
        raise ValueError("property must be followed by a value")
    value, input_string = parse_value(input_string[1:])
    if input_string[0] != "]":
        raise ValueError("property value must be enclosed in square brackets")
    return key, value, input_string[1:]

def parse_value(input_string):
    value = ""
    while input_string and input_string[0] != "]":
        if input_string[0] == "\\":
            if len(input_string) == 1:
                raise ValueError("invalid escape sequence")
            value += input_string[1]
            input_string = input_string[2:]
        else:
            value += input_string[0]
            input_string = input_string[1:]
    return value, input_string[1:]
