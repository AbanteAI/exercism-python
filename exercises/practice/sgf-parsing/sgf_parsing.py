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

import re

class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        return self.properties == other.properties and self.children == other.children

    def __ne__(self, other):
        return not self == other

def parse(input_string):
    if not input_string:
        raise ValueError("tree missing")
    if not input_string.startswith('(') or not input_string.endswith(')'):
        raise ValueError("properties without delimiter")
    if input_string.count('(') != input_string.count(')'):
        raise ValueError("tree missing")
    
    input_string = input_string.strip()
    # Remove the leading and trailing parentheses
    input_string = input_string[1:-1].strip()
    
    # Check if the input string is empty after removing parentheses
    if not input_string:
        raise ValueError("tree with no nodes")
    
    # Split the input string into parts based on semicolon
    parts = input_string.split(';')
    
    # Remove empty strings from parts
    parts = [part for part in parts if part]
    
    # Check if there are no nodes after splitting
    if not parts:
        raise ValueError("tree with no nodes")
    
    # Parse the properties and construct the SgfTree
    root_properties = parse_properties(parts[0])
    children = [parse(child) for child in find_children(parts[1:])]
    return SgfTree(properties=root_properties, children=children)

def parse_properties(properties_string):
    properties = {}
    # Match all property patterns
    for match in re.finditer(r'([A-Z]+)\[((?:[^\\\]]|\\.)*)\]', properties_string):
        key, values = match.groups()
        values = values.split('][')
        values = [value.replace('\\', '') for value in values]
        # Add the property to the dictionary, handling multiple values
        if key in properties:
            properties[key].extend(values)
        else:
            properties[key] = values
    return properties

def find_children(parts):
    # This function will find child nodes and return them as a list of strings
    # For simplicity, this example assumes that there are no variations (branches)
    # This will need to be expanded to handle variations correctly
    return parts
