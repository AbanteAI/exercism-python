class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

def __eq__(self, other):
    if not isinstance(other, SgfTree):
        return False
    if self.properties != other.properties:
        return False
    if len(self.children) != len(other.children):
        return False
    for child, other_child in zip(self.children, other.children):
        if child != other_child:
            return False
    return True

    def __ne__(self, other):
        return not self == other


def parse_properties(input_string, index):
    properties = {}
    while input_string[index] != ';' and input_string[index] != '(' and input_string[index] != ')':
        key = input_string[index:index+2]
        index += 2
        values = []
        while input_string[index] == '[':
            index += 1
            value = []
            while input_string[index] != ']':
                if input_string[index] == '\\':
                    index += 1
                value.append(input_string[index])
                index += 1
            index += 1
            values.append(''.join(value))
        properties[key] = values
    return properties, index

def parse_node(input_string, index):
    if input_string[index] == ';':
        index += 1
        properties, index = parse_properties(input_string, index)
        node = SgfTree(properties)
        while input_string[index] == '(':
            index += 1
            child, index = parse_node(input_string, index)
            node.children.append(child)
            index += 1
        return node, index
    return None, index

def parse(input_string):
    if input_string[0] != '(' or input_string[-1] != ')':
        raise ValueError("Invalid SGF string")
    tree, index = parse_node(input_string, 1)
    if index != len(input_string) - 1:
        raise ValueError("Invalid SGF string")
    return tree
def parse(input_string):
    pass
