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
    tree = SgfTree()
    current_node = tree

    # Remove any leading and trailing whitespace from the input string
    input_string = input_string.strip()

    # Remove any newlines immediately after a backslash
    input_string = input_string.replace("\\\n", "")

    # Replace all other whitespace characters with spaces
    input_string = input_string.replace("\t", " ").replace("\r", " ")

    # Process the input string character by character
    i = 0
    while i < len(input_string):
        c = input_string[i]

        if c == "(":
            # Start of a new node
            new_node = SgfTree()
            current_node.children.append(new_node)
            current_node = new_node
        elif c == ")":
            # End of the current node
            current_node = current_node.parent
        elif c.isalpha():
            # Property key
            key = ""
            while i < len(input_string) and input_string[i].isalpha():
                key += input_string[i]
                i += 1

            # Property values
            values = []
            while i < len(input_string) and input_string[i] == "[":
                value = ""
                i += 1
                while i < len(input_string) and input_string[i] != "]":
                    value += input_string[i]
                    i += 1
                values.append(value)
                i += 1

            # Add the property to the current node
            current_node.properties[key] = values

            # Adjust the index to skip the closing bracket
            i += 1
        else:
            # Ignore other characters
            i += 1

    return tree