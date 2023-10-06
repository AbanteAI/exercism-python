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
    if not input_string.startswith('(') or not input_string.endswith(')'):
        raise ValueError("input is not a tree")
    
    input_string = input_string[1:-1]
    properties, children = parse_node(input_string)
    return SgfTree(properties, children)

def parse_node(input_string):
    properties = {}
    children = []
    while input_string:
        if input_string[0] == '(':
            child, input_string = parse_node(input_string[1:])
            children.append(child)
        elif input_string[0] == ')':
            return properties, children
        else:
            key, input_string = parse_property(input_string)
            values, input_string = parse_values(input_string)
            properties[key] = values

    raise ValueError("input is not a tree")

def parse_property(input_string):
    if not input_string.startswith(';'):
        raise ValueError("property missing")
    
    input_string = input_string[1:]
    key, input_string = parse_key(input_string)
    return key, input_string

def parse_key(input_string):
    if not input_string:
        raise ValueError("property key missing")
    
    key = ""
    while input_string and input_string[0].isalpha():
        key += input_string[0]
        input_string = input_string[1:]
    
    if not key.isupper():
        raise ValueError("property must be in uppercase")
    
    return key, input_string

def parse_values(input_string):
    if not input_string.startswith('['):
        raise ValueError("property values missing")
    
    input_string = input_string[1:]
    values, input_string = parse_value(input_string)
    return values, input_string

def parse_value(input_string):
    if not input_string:
        raise ValueError("property value missing")
    
    value = ""
    while input_string:
        if input_string[0] == ']':
            return value, input_string[1:]
        elif input_string[0] == '\\':
            value += input_string[1]
            input_string = input_string[2:]
        else:
            value += input_string[0]
            input_string = input_string[1:]
    
    raise ValueError("property value missing")

