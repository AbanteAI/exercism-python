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
        raise ValueError("No records to build a tree with.")

    records.sort(key=lambda record: record.record_id)
    nodes = [None] * len(records)

    for record in records:
        record_id = record.record_id
        parent_id = record.parent_id

        if record_id < 0 or record_id >= len(records):
            raise ValueError("Record ID out of bounds.")
        if record_id < parent_id:
            raise ValueError("Parent ID must be lower than Record ID.")
        if record_id == parent_id and record_id != 0:
            raise ValueError("Only root should have equal record and parent id.")
        if parent_id > record_id:
            raise ValueError("Tree is a cycle.")
        if record_id != 0 and nodes[parent_id] is None:
            raise ValueError("Parent node does not exist.")

        node = Node(record_id)
        nodes[record_id] = node

        if record_id != 0:
            nodes[parent_id].children.append(node)

    if nodes[0] is None:
        raise ValueError("Root node not found.")

    return nodes[0]
