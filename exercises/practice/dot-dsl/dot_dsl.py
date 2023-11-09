NODE, EDGE, ATTR = range(3)


class Node:
    def __init__(self, name, attrs):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge:
    def __init__(self, src, dst, attrs):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


class Graph:
    def __init__(self, data=None):
        if data is None:
            self.nodes = []
            self.edges = []
            self.attrs = {}
        elif isinstance(data, list):
            self._parse_data(data)
        else:
            raise TypeError("Graph data must be a list")

    def _parse_data(self, data):
        self.nodes = []
        self.edges = []
        self.attrs = {}
        for item in data:
            if not isinstance(item, tuple) or len(item) < 2:
                raise TypeError("Malformed graph component")
            item_type, *item_values = item
            if item_type == NODE:
                self._add_node(item_values)
            elif item_type == EDGE:
                self._add_edge(item_values)
            elif item_type == ATTR:
                self._add_attr(item_values[0], item_values[1])

    def _add_node(self, values):
        if len(values) != 2 or not isinstance(values[0], str) or not isinstance(values[1], dict):
            raise ValueError("Node malformed")
        self.nodes.append(Node(*values))

    def _add_edge(self, values):
        if len(values) != 3 or not isinstance(values[0], str) or not isinstance(values[1], str) or not isinstance(values[2], dict):
            raise ValueError("Edge malformed")
        self.edges.append(Edge(*values))

    def _add_attr(self, key, value):
        if not isinstance(key, str):
            raise ValueError("Attribute key must be a string")
        self.attrs[key] = value

    def __eq__(self, other):
        return (self.nodes == other.nodes and
                self.edges == other.edges and
                self.attrs == other.attrs)
