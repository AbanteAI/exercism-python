class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def build_tree(records):
    if not records:
        return None

    records.sort(key=lambda r: r.record_id)

    if records[0].record_id != 0 or records[0].parent_id != 0:
        raise ValueError("Invalid root record")

    tree_nodes = {record.record_id: Node(record.record_id) for record in records}

    for record in records:
        if record.record_id == 0:
            continue

        if record.record_id <= record.parent_id:
            raise ValueError("Invalid record: parent_id must be less than record_id")

        parent_node = tree_nodes[record.parent_id]
        child_node = tree_nodes[record.record_id]
        parent_node.children.append(child_node)

    return tree_nodes[0]