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
            data = []

        self.nodes = []
        self.edges = []
        self.attrs = {}

        for item in data:
            if len(item) < 2:
                raise ValueError("Item malformed")

            item_type, item_data = item[0], item[1:]

            if item_type == NODE:
                if len(item_data) != 2:
                    raise ValueError("NODE malformed")
                name, attrs = item_data
                self.nodes.append(Node(name, attrs))
            elif item_type == EDGE:
                if len(item_data) != 3:
                    raise ValueError("Edge is malformed")
                src, dst, attrs = item_data
                self.edges.append(Edge(src, dst, attrs))
            elif item_type == ATTR:
                key, value = item_data
                self.attrs[key] = value
            else:
                raise TypeError("Graph data malformed")
