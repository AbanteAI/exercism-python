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
def parse(input_string):
    if not input_string.startswith("(") or not input_string.endswith(")"):
        raise ValueError("tree missing")

    stack = []
    tree = SgfTree()
    current_tree = tree
    index = 1
    while index < len(input_string) - 1:
        char = input_string[index]
        if char == ";":
            properties = {}
            index += 1
            while index < len(input_string) - 1 and input_string[index] != "(" and input_string[index] != ")":
                if input_string[index].isupper():
                    prop = input_string[index]
                    index += 1
                    if input_string[index] != "[":
                        raise ValueError("properties without delimiter")
                    values = []
                    while input_string[index] == "[":
                        index += 1
                        value = []
                        while input_string[index] != "]":
                            if input_string[index] == "\\":
                                index += 1
                                if input_string[index] == "]":
                                    value.append(input_string[index])
                                elif input_string[index] in ["n", "t"]:
                                    value.append(" ")
                                else:
                                    value.append(input_string[index])
                            else:
                                value.append(input_string[index])
                            index += 1
                        values.append("".join(value))
                        index += 1
                    properties[prop] = values
                else:
                    raise ValueError("property must be in uppercase")
            current_tree.properties.update(properties)
        elif char == "(":
            new_tree = SgfTree()
            current_tree.children.append(new_tree)
            stack.append(current_tree)
            current_tree = new_tree
            index += 1
        elif char == ")":
            if not stack:
                raise ValueError("tree with no nodes")
            current_tree = stack.pop()
            index += 1
        else:
            raise ValueError("invalid character")

    if stack:
        raise ValueError("tree with no nodes")

    return tree