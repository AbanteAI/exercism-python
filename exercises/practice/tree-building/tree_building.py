class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    if not records:
        return None

    for record in records:
        if record.record_id not in nodes:
            nodes[record.record_id] = Node(record.record_id)

        node = nodes[record.record_id]

        if record.parent_id != record.record_id:
            if record.parent_id >= record.record_id:
                raise ValueError("Parent ID must be lower than record ID")
            parent = nodes.setdefault(record.parent_id, Node(record.parent_id))
            parent.children.append(node)
            if node in parent.children:
                raise ValueError("Cycle detected in tree")

    return nodes[0]

    return nodes[0]