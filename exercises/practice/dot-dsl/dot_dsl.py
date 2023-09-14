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
        if data:
        for item in data:
            if len(item) < 2:
                raise ValueError("Malformed graph item")

            if item[0] == NODE:
                if len(item) != 3:
                    raise ValueError("Malformed node")
                self.add_node(item[1], item[2])
            elif item[0] == EDGE:
                if len(item) != 4:
                    raise ValueError("Malformed edge")
                self.add_edge(item[1], item[2], item[3])
            elif item[0] == ATTR:
                if len(item) != 3:
                    raise ValueError("Malformed attribute")
                self.add_attr(item[1], item[2])
            else:
                raise ValueError("Unknown graph item")

    def add_node(self, name, attrs):
        self.nodes.append(Node(name, attrs))

    def add_edge(self, src, dst, attrs):
        self.edges.append(Edge(src, dst, attrs))

    def add_attr(self, key, value):
        self.attrs[key] = value

    def set_node_attr(self, name, key, value):
        for node in self.nodes:
            if node.name == name:
                node.attrs[key] = value
                break

    def set_edge_attr(self, src, dst, key, value):
        for edge in self.edges:
            if edge.src == src and edge.dst == dst:
                edge.attrs[key] = value
                break
