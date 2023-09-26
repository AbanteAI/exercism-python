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
    def parse_node(node_string):
        properties = {}
        children = []

        while node_string:
            if node_string[0] == ";":
                node_string = node_string[1:]
                key = ""
                value = ""
                in_key = True
                in_value = False
                escaped = False

                for char in node_string:
                    if in_key:
                        if char == "[":
                            in_key = False
                            in_value = True
                        else:
                            key += char
                    elif in_value:
                        if escaped:
                            if char != "\\" and char != "]":
                                value += "\\"
                            value += char
                            escaped = False
                        elif char == "\\":
                            escaped = True
                        elif char == "]":
                            properties.setdefault(key, []).append(value)
                            key = ""
                            value = ""
                            in_key = True
                            in_value = False
                        else:
                            value += char
                    else:
                        break

                node_string = node_string[len(key) + len(value) + 3:]
            elif node_string[0] == "(":
                node_string = node_string[1:]
                child, node_string = parse_node(node_string)
                children.append(child)
            elif node_string[0] == ")":
                node_string = node_string[1:]
                break
            else:
                node_string = node_string[1:]

        return SgfTree(properties, children), node_string

    input_string = input_string.replace("\r\n", "\n").replace("\r", "\n")
    input_string = input_string.replace("\\\n", "").replace("\\\r", "").replace("\\\r\n", "")
    input_string = input_string.replace("\n", "").replace("\t", " ").replace("\f", " ").replace("\v", " ")
    input_string = input_string.replace("\\\\", "\\")

    return parse_node(input_string)[0]
