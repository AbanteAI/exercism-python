class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def validate_records(records):
    record_ids = set()
    parent_ids = set()
    for record in records:
        record_ids.add(record.record_id)
        parent_ids.add(record.parent_id)
        if record.record_id == 0 and record.parent_id != 0:
            raise ValueError('Root record should have parent ID equal to its own ID')
        if record.record_id < record.parent_id:
            raise ValueError('Record ID should be greater than or equal to its parent ID')
    if len(record_ids) != len(records) or len(parent_ids) != len(records):
        raise ValueError('Duplicate record IDs or parent IDs found')
    if len(record_ids - parent_ids) != 1:
        raise ValueError('Invalid tree structure')
    return record_ids
def BuildTree(records):
    validate_records(records)
    record_ids = {record.record_id: Node(record.record_id) for record in records}
    for record in records:
        if record.parent_id != record.record_id:
            record_ids[record.parent_id].children.append(record_ids[record.record_id])
    return record_ids[0]
