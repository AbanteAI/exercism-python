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
        raise ValueError("tree missing")
    if not input_string.isupper():
        raise ValueError("property must be in uppercase")

    # Remove the leading and trailing parentheses
    input_string = input_string[1:-1].strip()

    # Check if the input string is empty after removing parentheses
    if not input_string:
        raise ValueError("tree with no nodes")

    # Initialize the root node
    root_properties = {}
    children = []
    current_node = SgfTree(properties=root_properties, children=children)

    # Parse the input string
    # This is a placeholder for the actual parsing logic that will be implemented
    # ...

    # Implement parsing of properties and values
    while input_string:
        if input_string[0] != ';':
            raise ValueError("each node must start with a semicolon")
        input_string = input_string[1:].strip()
        properties = {}
        while input_string and input_string[0].isalpha():
            end_of_key = input_string.find('[')
            key = input_string[:end_of_key]
            input_string = input_string[end_of_key:]
            values = []
            while input_string.startswith('['):
                end_of_value = input_string.find(']')
                if end_of_value == -1:
                    raise ValueError("property values must be enclosed in brackets")
                value = input_string[1:end_of_value]
                # Handle escaped characters
                value = value.replace('\\\\', '\\').replace('\\]', ']').replace('\\\n', '')
                values.append(value)
                input_string = input_string[end_of_value+1:].strip()
            properties[key] = values
        current_node.properties = properties
        # Check for child nodes
        if input_string.startswith('('):
            child_nodes = []
            while input_string.startswith('('):
                end_of_child = input_string.find(')')
                if end_of_child == -1:
                    raise ValueError("child nodes must be enclosed in parentheses")
                child_string = input_string[1:end_of_child]
                child_nodes.append(parse(child_string))
                input_string = input_string[end_of_child+1:].strip()
            current_node.children = child_nodes
        elif input_string:
            raise ValueError("invalid structure")

    return current_node
# Removed placeholder comment
#
