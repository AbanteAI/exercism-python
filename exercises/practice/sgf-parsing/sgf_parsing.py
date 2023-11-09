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
    if not input_string.startswith('(') or not input_string.endswith(')'):
        raise ValueError("tree missing")
    
    input_string = input_string.strip('()')
    properties = {}
    children = []
    current_node = None

    # Regular expression patterns for parsing
    prop_pattern = re.compile(r'([A-Z]+)((?:\[.*?(?<!\\)\])+)')
    node_pattern = re.compile(r';')

    def parse_properties(prop_string):
        props = {}
        for match in re.finditer(r'\[.*?(?<!\\)\]', prop_string):
            value = match.group(0).strip('[]')
            # Handle escape characters
            value = re.sub(r'\\(.)', r'\1', value)
            props.setdefault(prop_key, []).append(value)
        return props

    while input_string:
        node_match = node_pattern.match(input_string)
        if node_match:
            if current_node:
                children.append(current_node)
            current_node = {'properties': {}, 'children': []}
            input_string = input_string[node_match.end():]
        else:
            prop_match = prop_pattern.match(input_string)
            if prop_match:
                prop_key, prop_values = prop_match.groups()
                if not prop_key.isupper():
                    raise ValueError("property must be in uppercase")
                current_node['properties'].update(parse_properties(prop_values))
                input_string = input_string[prop_match.end():]
            else:
                raise ValueError("properties without delimiter")

    if current_node:
        children.append(current_node)

    if not children:
        raise ValueError("tree with no nodes")

    # Convert the parsed properties and children into SgfTree objects
    def build_tree(node):
        return SgfTree(properties=node['properties'], children=[build_tree(child) for child in node['children']])

    return build_tree(children[0])
