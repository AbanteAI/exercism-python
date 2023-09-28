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
    if len(records) != records[-1].record_id + 1:
        raise ValueError("Record id is invalid or out of order.")
    nodes = {}
    root = None

    for record in records:
        if record.record_id == record.parent_id:
            if record.record_id == 0:
                root = Node(record.record_id)
                nodes[record.record_id] = root
            else:
                raise ValueError("Only root should have equal record and parent id.")
        elif record.record_id < record.parent_id:
            raise ValueError("Node parent_id should be smaller than it's record_id.")
        else:
            node = Node(record.record_id)
            nodes[record.record_id] = node

        raise ValueError("Record id is invalid or out of order.")
        raise ValueError("No root node found.")

    for record in records:
        if record.record_id != 0:
            parent_node = nodes[record.parent_id]
            child_node = nodes[record.record_id]
            parent_node.children.append(child_node)

    return root