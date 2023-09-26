from collections import defaultdict

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
        return (
            self.src == other.src
            and self.dst == other.dst
            and self.attrs == other.attrs
        )


class Graph:
    def __init__(self, data=None):
        self.nodes = []
        self.edges = []
        self.attributes = defaultdict(dict)

        if data:
            self.parse_dsl(data)

    def parse_dsl(self, data):
        lines = data.strip().split("\n")
        for line in lines:
            line = line.strip()
            if line.startswith("graph"):
                self.parse_graph_attributes(line[5:].strip())
            elif line.startswith(("node", "edge")):
                self.parse_element(line)

    def parse_graph_attributes(self, attributes):
        for attr in attributes.split(","):
            key, value = attr.split("=")
            self.attributes["graph"][key.strip()] = value.strip()

    def parse_element(self, line):
        element_type, element_name, attributes = self.extract_element_parts(line)

        if element_type == "node":
            self.nodes.append(Node(element_name, self.parse_attributes(attributes)))
        elif element_type == "edge":
            src, dst = element_name.split("--")
            self.edges.append(
                Edge(src.strip(), dst.strip(), self.parse_attributes(attributes))
            )

    def extract_element_parts(self, line):
        element_type, element_name_attributes = line.split(" ", 1)
        element_name, attributes = element_name_attributes.split("[", 1)
        return element_type.strip(), element_name.strip(), attributes.rstrip("]")

    def parse_attributes(self, attributes):
        parsed_attrs = {}
        for attr in attributes.split(","):
            key, value = attr.split("=")
            parsed_attrs[key.strip()] = value.strip()
        return parsed_attrs