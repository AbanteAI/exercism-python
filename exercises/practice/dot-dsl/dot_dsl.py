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
    def add_node(self, name, attrs):
        if not isinstance(name, str) or not isinstance(attrs, dict):
            raise ValueError("Node parameters are malformed")
        self.nodes.append(Node(name, attrs))

    def add_edge(self, src, dst, attrs=None):
        if not (isinstance(src, str) and isinstance(dst, str) and (isinstance(attrs, dict) or attrs is None)):
            raise ValueError("Edge parameters are malformed")
        self.edges.append(Edge(src, dst, attrs or {}))

    def add_attr(self, key, value):
        if not (isinstance(key, str) and isinstance(value, str)):
            raise ValueError("Attribute parameters are malformed")
        if len(value) > 2:
            raise ValueError("Attribute parameters are malformed")
        self.attrs[key] = value
    def __init__(self, data=None):
        self.nodes = []
        self.edges = []
        self.attrs = {}

        if data:
            for item in data:
                if len(item) < 2:
                    raise ValueError("Item in data is malformed")
                item_type, *item_data = item

                if item_type == NODE:
                    self.add_node(*item_data)
                elif item_type == EDGE:
                    self.add_edge(*item_data)
                elif item_type == ATTR:
                    self.add_attr(*item_data)
                else:
                    raise TypeError("Invalid item type in data")