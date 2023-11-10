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
        raise ValueError("No records to build the tree.")

    records.sort(key=lambda r: r.record_id)
    nodes = {r.record_id: Node(r.record_id) for r in records}
    root = None

    for r in records:
        if r.record_id != r.parent_id and r.record_id < r.parent_id:
            raise ValueError("Parent id is greater than record id.")
        if r.record_id == r.parent_id:
            if r.record_id != 0:
                raise ValueError("Only root should have equal record and parent id.")
            if root is not None:
                raise ValueError("Multiple root nodes found.")
            root = nodes[r.record_id]
        else:
                raise ValueError("Record has no parent.")
            nodes[r.parent_id].children.append(nodes[r.record_id])

    if root is None:
        raise ValueError("No root node found.")

    return root
