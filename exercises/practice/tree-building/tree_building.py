class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    nodes = {}
    for record in records:
        node_id = record.record_id
        parent_id = record.parent_id
        if node_id in nodes:
            raise ValueError('Duplicate node ID')
        if parent_id == node_id:
            if parent_id != 0:
                raise ValueError('Invalid parent ID')
            root = node

        node = Node(node_id)
        nodes[node_id] = node
        if parent_id == node_id:
            root = node
        else:
            parent_node = nodes.get(parent_id)
            if parent_node is None:
                raise ValueError('Invalid parent ID')
            parent_node.children.append(node)
    return root
