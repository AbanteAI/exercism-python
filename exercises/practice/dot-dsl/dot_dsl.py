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
        self.nodes = []
        self.edges = []
        self.attrs = {}

        if data is not None:
            if not isinstance(data, list):
                raise TypeError("Graph data malformed")

            for item in data:
                if not isinstance(item, tuple) or len(item) < 2:
                    raise TypeError("Graph item incomplete")

                item_type, *item_data = item

                if item_type == NODE:
                    if len(item_data) != 2:
                        raise ValueError("Node is malformed")
                    name, attrs = item_data
                    self.nodes.append(Node(name, attrs))
                elif item_type == EDGE:
                    if len(item_data) != 3:
                        raise ValueError("Edge is malformed")
                    src, dst, attrs = item_data
                    self.edges.append(Edge(src, dst, attrs))
                elif item_type == ATTR:
                    if len(item_data) != 2:
                        raise ValueError("Attribute is malformed")
                    key, value = item_data
                    self.attrs[key] = value
                else:
                    raise ValueError("Unknown item")