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
    def parse_property_list(property_list):
        properties = {}
        while property_list:
            key, property_list = parse_property(property_list)
            values, property_list = parse_values(property_list)
            properties[key] = values
        return properties

    def parse_property(property_list):
        key = property_list[0]
        return key, property_list[1:]

    def parse_values(property_list):
        values = []
        while property_list and property_list[0] != ']':
            if property_list[0] == '[':
                value, property_list = parse_value(property_list[1:])
                values.append(value)
            else:
                    raise ValueError("property must be in uppercase")
        if property_list and property_list[0] == ']':
            return values, property_list[1:]
        else:
            raise ValueError("Invalid property values")

    def parse_value(property_list):
        value = ""
        while property_list and property_list[0] != ']':
            if property_list[0] == '\\':
                if len(property_list) > 1:
                    value += property_list[1]
                    property_list = property_list[2:]
                else:
                    raise ValueError("Invalid property values")
            else:
                value += property_list[0]
                property_list = property_list[1:]
        if property_list and property_list[0] == ']':
            return value, property_list[1:]
        else:
            raise ValueError("Invalid property values")

    property_list = list(input_string)
    tree = SgfTree()
    current_node = tree
    while property_list:
        if property_list[0] == '(':
            property_list = property_list[1:]
            child_node = SgfTree()
            current_node.children.append(child_node)
            current_node = child_node
        elif property_list[0] == ')':
            property_list = property_list[1:]
            if current_node == tree:
                raise ValueError("Invalid property list")
            current_node = current_node.parent
        else:
            properties = parse_property_list(property_list)
            current_node.properties.update(properties)
    if current_node != tree:
        raise ValueError("Invalid property list")
    return tree.children[0]