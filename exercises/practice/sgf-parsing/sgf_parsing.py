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
    if not input_string:
        raise ValueError("tree missing")
    if not input_string.startswith('(') or not input_string.endswith(')'):
        raise ValueError("tree missing")
    
    input_string = input_string.strip('()')
    properties = {}
    children = []
    current_node_properties = None

    parts = input_string.split(';')
    for part in parts:
        if part.startswith('('):
            children.append(parse(part))
        elif part:
            key_values = part.split(']')
            for key_value in key_values:
                if not key_value:
                    continue
                key, value = key_value.split('[', 1)
                if not key.isupper():
                    raise ValueError("property must be in uppercase")
                if '\\' in value:
                    value = value.replace('\\\\', '\\').replace('\\]', ']')
                if current_node_properties is not None:
                    properties = current_node_properties
                    current_node_properties = None
                if key in properties:
                    properties[key].append(value)
                else:
                    properties[key] = [value]
        elif current_node_properties is not None:
            raise ValueError("tree with no nodes")
        else:
            current_node_properties = {}

    if not properties and not children:
        raise ValueError("tree with no nodes")

    return SgfTree(properties=properties, children=children)
