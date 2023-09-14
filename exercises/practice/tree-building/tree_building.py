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

    records.sort(key=lambda record: record.record_id)

    if records[0].record_id != 0 or records[0].parent_id != 0:
        raise ValueError("Invalid root record.")

    nodes = {}
    for record in records:
        if record.record_id == record.parent_id and record.record_id != 0:
            raise ValueError("A node cannot be its own parent, except for the root node.")

        if record.record_id < record.parent_id:
            raise ValueError("A node's parent_id must be less than the node's record_id.")

        if record.record_id != len(nodes):
            raise ValueError("Non-continuous records found.")

        nodes[record.record_id] = Node(record.record_id)

        if record.record_id != 0:
            parent_node = nodes[record.parent_id]
            parent_node.children.append(nodes[record.record_id])

    return nodes[0]