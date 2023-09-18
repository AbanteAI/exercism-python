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
    def parse_properties(properties_string):
        properties = {}
        for key, values in re.findall(r"([A-Za-z]+)\[([^\]]*)\]", properties_string):
            if key.islower():
                raise ValueError("property must be in uppercase")
            properties[key] = [re.sub(r"\\\n", "", value.replace("\\", "")) for value in re.split(r"(?<!\\)\]", values) if value]

        return properties

    def parse_nodes(node_string):
        stack = []
        current_node = None
        i = 0

        while i < len(node_string):
            char = node_string[i]
            if char == "(":
                stack.append(SgfTree())
            elif char == ";":
                current_node = SgfTree()
                if stack:
                    stack[-1].children.append(current_node)
            elif char == "[":
                if current_node is not None:
                    properties_start = node_string.rfind(";", 0, i) + 1
                    current_node.properties = parse_properties(node_string[properties_start:i])
                    i = node_string.index("]", i) + 1
                    current_node = None
                    continue
            elif char == ")":
                finished_node = stack.pop()
                if not stack:
                    return finished_node
            i += 1

        raise ValueError("Invalid input string")

    if not input_string:
        raise ValueError("tree missing")

    if not input_string.startswith("(") or not input_string.endswith(")"):
        raise ValueError("Invalid input string")

    return parse_nodes(input_string[1:-1])
            i += 1

        raise ValueError("Invalid input string")

    if not input_string.startswith("(") or not input_string.endswith(")"):
        raise ValueError("Invalid input string")

    return parse_nodes(input_string[1:-1])