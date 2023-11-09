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
            if not isinstance(item, tuple):
                raise TypeError("Malformed graph component")
            descriptor = item[0]
            if descriptor == NODE and len(item) == 3:
                self._add_node(item[1:])
            elif descriptor == EDGE and len(item) == 4:
                self._add_edge(item[1:])
            elif descriptor == ATTR and len(item) == 3:
                self._add_attr(item[1:])
            else:
                raise ValueError("Invalid graph component descriptor or wrong tuple size")
            descriptor, value = item
            if descriptor == NODE:
                self._add_node(value)
            elif descriptor == EDGE:
                self._add_edge(value)
            elif descriptor == ATTR:
                self._add_attr(value)
            else:
                raise ValueError("Invalid graph component descriptor")

    def _add_node(self, value):
        name, attrs = value
        if not (isinstance(name, str) and isinstance(attrs, dict)):
            raise ValueError("Node name must be a string and attrs must be a dict")
        self.nodes.append(Node(name, attrs))
        self.nodes.append(Node(name, attrs))

    def _add_edge(self, value):
        src, dst, attrs = value
        if not (isinstance(src, str) and isinstance(dst, str) and isinstance(attrs, dict)):
            raise ValueError("Edge src and dst must be strings and attrs must be a dict")
        self.edges.append(Edge(src, dst, attrs))
        self.edges.append(Edge(src, dst, attrs))

    def _add_attr(self, value):
        key, val = value
        self.attrs[key] = val

    def __eq__(self, other):
        return (self.nodes == other.nodes and
                self.edges == other.edges and
                self.attrs == other.attrs)
