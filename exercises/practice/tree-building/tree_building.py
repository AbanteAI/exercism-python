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

    records.sort(key=lambda x: x.record_id)
    nodes = {record.record_id: Node(record.record_id) for record in records}

    root = None
    for record in records:
        if record.record_id == record.parent_id:
            if record.record_id != 0:
                raise ValueError("Only root should have equal record and parent id.")
            root = nodes[record.record_id]
            continue

        parent_node = nodes.get(record.parent_id)
        if not parent_node:
            raise ValueError("Node parent_id should be smaller than it's record_id.")

        parent_node.children.append(nodes[record.record_id])

    return root
