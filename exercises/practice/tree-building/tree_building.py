class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []

def BuildTree(records):
    records.sort(key=lambda x: x.record_id)
    if not records or records[0].record_id != 0:
        raise ValueError('invalid')

    nodes = {0: Node(0)}
    for record in records[1:]:
        if record.record_id < record.parent_id:
            raise ValueError('something went wrong!')
        if record.record_id in nodes:
            raise ValueError('duplicate record ID')

        node = Node(record.record_id)
        nodes[record.record_id] = node
        parent = nodes.get(record.parent_id)
        if parent is None:
            raise ValueError('broken tree')
        parent.children.append(node)

    return nodes[0]