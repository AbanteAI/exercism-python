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
        raise ValueError("No records provided")

    records.sort(key=lambda r: r.record_id)

    if records[0].record_id != 0 or records[0].parent_id != 0:
        raise ValueError("Root record must have record_id and parent_id of 0")

    nodes = {}
    for record in records:
        if record.record_id >= len(records) or record.record_id < record.parent_id:
            raise ValueError("Record id must be greater than parent id and less than the length of records")
        if record.record_id == record.parent_id and record.record_id != 0:
            raise ValueError("Only root should have equal record and parent id")

        nodes[record.record_id] = Node(record.record_id)

        nodes[record.record_id] = Node(record.record_id)

        if record.record_id != 0:
            parent_node = nodes.get(record.parent_id)
            if parent_node is None:
                raise ValueError("Parent id must be lower than record id and not greater than the largest id")
            parent_node.children.append(nodes[record.record_id])

    return nodes[0]
