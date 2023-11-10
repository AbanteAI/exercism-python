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
            self.nodes = [Node(name, attrs) for name, type_, attrs in data if type_ == NODE and len(item) == 3]
            self.edges = [Edge(src, dst, attrs) for src, dst, type_, attrs in data if type_ == EDGE and len(item) == 4]
            self.attrs = {attr: value for attr, type_, value in data if type_ == ATTR and len(item) == 3]
            self._validate_data(data)
        else:
            raise TypeError("Graph data must be a list of tuples")

    def _validate_data(self, data):
        for item in data:
            if not isinstance(item, tuple):
                raise TypeError("Graph data malformed, each item must be a tuple")
                if type_ == NODE and len(item) != 3:
                    raise TypeError("Node tuples must have 3 elements")
                if type_ == EDGE and len(item) != 4:
                    raise TypeError("Edge tuples must have 4 elements")
                if type_ == ATTR and len(item) != 3:
                    raise TypeError("Attribute tuples must have 3 elements")
                type_ = item[1]
                raise TypeError("Graph data malformed, each tuple must have 3 elements")
            type_ = item[1]
            if type_ not in (NODE, EDGE, ATTR):
                raise TypeError("Graph data malformed, type must be NODE, EDGE, or ATTR")
            if type_ == NODE and not isinstance(item[0], str):
                raise ValueError("Node name must be a string")
            if type_ == EDGE and not (isinstance(item[0], str) and isinstance(item[1], str)):
                raise ValueError("Edge source and destination must be strings")
            if type_ == ATTR and not isinstance(item[0], str):
                raise ValueError("Attribute name must be a string")
            if type_ in (NODE, EDGE) and not isinstance(item[2], dict):
                raise ValueError("Attributes must be a dictionary")
