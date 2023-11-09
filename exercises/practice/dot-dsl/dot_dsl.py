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
            if not isinstance(item, tuple):
                raise TypeError("Malformed graph component")
            type_ = item[0]
            if type_ == NODE and len(item) == 3:
                _, name, attrs = item
                if not isinstance(name, str) or not isinstance(attrs, dict):
                    raise ValueError("Node must have a string name and a dict of attributes")
                self.nodes.append(Node(name, attrs))
            elif type_ == EDGE and len(item) == 4:
                _, nodes, attrs = item[0:3], item[3]
                if not (isinstance(nodes, tuple) and len(nodes) == 2 and all(isinstance(n, str) for n in nodes)):
                    raise ValueError("Edge must have a tuple of two string node names")
                if not isinstance(attrs, dict):
                    raise ValueError("Edge attributes must be a dict")
                self.edges.append(Edge(*nodes, attrs))
            elif type_ == ATTR and len(item) == 3:
                _, key, value = item
                if not isinstance(key, str):
                    raise ValueError("Attribute name must be a string")
                self.attrs[key] = value
            else:
                raise TypeError("Invalid graph component type")
