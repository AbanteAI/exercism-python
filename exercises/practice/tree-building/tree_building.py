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
    ordered_id = [i.record_id for i in records]

    if ordered_id[-1] != len(ordered_id) - 1:
        raise ValueError("Record id is invalid or out of order.")
    if ordered_id[0] != 0:
        raise ValueError('invalid')

    nodes = {record.record_id: Node(record.record_id) for record in records}

    for record in records:
        if record.record_id == 0:
            if record.parent_id != 0:
                raise ValueError("Node parent_id should be smaller than it's record_id.")
        elif record.record_id < record.parent_id:
            raise ValueError("Node parent_id should be smaller than it's record_id.")
        elif record.record_id == record.parent_id and record.record_id != 0:
            raise ValueError('error!')
        else:
            parent_node = nodes[record.parent_id]
            child_node = nodes[record.record_id]
            parent_node.children.append(child_node)

    return nodes[0]