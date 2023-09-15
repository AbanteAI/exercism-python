class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def validate_records(records):
    if not records:
        return
    ordered_ids = sorted(record.record_id for record in records)
    if ordered_ids[-1] != len(ordered_ids) - 1:
        raise ValueError('broken tree')
    if ordered_ids[0] != 0:
        raise ValueError('invalid')
    for record in records:
        if record.record_id < record.parent_id:
            raise ValueError('something went wrong!')
        if record.record_id == record.parent_id and record.record_id != 0:
            raise ValueError('error!')
        if record.record_id == 0 and record.parent_id != 0:
            raise ValueError('error!')

def BuildTree(records):
    validate_records(records)

    nodes = {record.record_id: Node(record.record_id) for record in records}
    root = None

    for record in records:
        if record.record_id == 0:
            root = nodes[record.record_id]
        else:
            parent = nodes[record.parent_id]
            parent.children.append(nodes[record.record_id])

    for node in nodes.values():
        node.children.sort(key=lambda child: child.node_id)

    return root