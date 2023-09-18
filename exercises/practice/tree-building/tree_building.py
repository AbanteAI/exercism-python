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
    if records[0].record_id != 0 or records[0].parent_id != 0:
        raise ValueError("Invalid root record")

    nodes = {record.record_id: Node(record.record_id) for record in records}
    root = nodes[0]

    for record in records:
        if record.record_id == 0:
            continue

        if record.parent_id > record.record_id:
            raise ValueError("Node parent_id should be smaller than it's record_id.")

        parent_node = nodes[record.parent_id]
        child_node = nodes[record.record_id]
        parent_node.children.append(child_node)

    return root