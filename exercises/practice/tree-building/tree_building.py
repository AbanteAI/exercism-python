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
    
    records_dict = {r.record_id: Node(r.record_id) for r in records}
    root = None
    for record in records:
        if record.record_id == 0 and record.parent_id != 0:
            raise ValueError('Root record must have parent ID equal to its own ID')
        
        if record.record_id < record.parent_id:
            raise ValueError('Record ID must be greater than or equal to parent ID')
        
        if record.record_id == record.parent_id:
            if record.record_id != 0:
                raise ValueError('Record cannot be its own parent')
        
        if record.record_id == 0:
            root = records_dict[record.record_id]
        else:
            parent = records_dict.get(record.parent_id)
            if parent is None:
                raise ValueError(f'Parent record with ID {record.parent_id} not found')
            parent.children.append(records_dict[record.record_id])
    
    if root is None:
        raise ValueError('Root record not found')
    
    return root
    if not records:
        return None
    
    records_dict = {r.record_id: Node(r.record_id) for r in records}
    root = None
    for record in records:
        if record.record_id == 0 and record.parent_id != 0:
            raise ValueError('Root record must have parent ID equal to its own ID')
        
        if record.record_id < record.parent_id:
            raise ValueError('Record ID must be greater than or equal to parent ID')
        
        if record.record_id == record.parent_id:
            if record.record_id != 0:
                raise ValueError('Record cannot be its own parent')
        
        if record.record_id == 0:
            root = records_dict[record.record_id]
        else:
            parent = records_dict.get(record.parent_id)
            if parent is None:
                raise ValueError(f'Parent record with ID {record.parent_id} not found')
            parent.children.append(records_dict[record.record_id])
    
    if root is None:
        raise ValueError('Root record not found')
    
    return root