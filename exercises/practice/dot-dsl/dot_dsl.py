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
        self.graph_attrs = []
        if data:
            for item in data:
                if item[0] == NODE:
                    self.add_node(item[1], item[2])
                elif item[0] == EDGE:
                    self.add_edge(item[1], item[2], item[3])
                elif item[0] == ATTR:
                    self.add_attr(item[1], item[2])

    def add_node(self, name, attrs):
        self.nodes.append(Node(name, attrs))

    def add_edge(self, src, dst, attrs):
        self.edges.append(Edge(src, dst, attrs))

    def add_attr(self, key, value):
        self.graph_attrs.append((key, value))

    def nodes(self):
        return self.nodes

    def edges(self):
        return self.edges

    def attrs(self):
        return self.graph_attrs