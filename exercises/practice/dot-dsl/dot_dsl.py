NODE, EDGE, ATTR = range(3)


class Node:
    def __init__(self, name, attrs=None):
        self.name = name
        self.attrs = attrs if attrs else {}

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge:
class Node:
    def __init__(self, name, attrs=None):
        self.name = name
        self.attrs = attrs if attrs else {}

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs
class Edge:
    def __init__(self, src, dst, attrs=None):
        self.src = src
        self.dst = dst
        self.attrs = attrs if attrs else {}

    def __eq__(self, other):
        return (
            self.src == other.src
            and self.dst == other.dst
            and self.attrs == other.attrs
        )
    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)

class Edge:
    def __init__(self, src, dst, attrs=None):
        self.src = src
        self.dst = dst
        self.attrs = attrs if attrs else {}

    def __eq__(self, other):
        return (
            self.src == other.src
            and self.dst == other.dst
            and self.attrs == other.attrs
        )

class Graph:
    def __init__(self, data=None):
class Graph:
    def __init__(self, data=None):
        self.nodes = []
        self.edges = []
        if data:
            for item in data:
                if isinstance(item, Node):
                    self.nodes.append(item)
                elif isinstance(item, Edge):
                    self.edges.append(item)

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, src, dst, attrs=None):
        edge = Edge(src, dst, attrs)
        self.edges.append(edge)