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
        elif not isinstance(data, list) or not all(isinstance(item, tuple) and len(item) == 3 for item in data):
            raise TypeError("Graph data malformed")
        else:
            self.nodes = [Node(name, attrs) for item_type, name, attrs in data if item_type == NODE]
            self.edges = [Edge(src, dst, attrs) for item_type, (src, dst), attrs in data if item_type == EDGE]
            self.attrs = dict(attrs for item_type, _, attrs in data if item_type == ATTR)

    def __eq__(self, other):
        return (self.nodes == other.nodes and
                self.edges == other.edges and
                self.attrs == other.attrs)
