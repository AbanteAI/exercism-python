def flatten(iterable):
    flattened = []
    for item in iterable:
        if item is None:
            continue
        elif isinstance(item, list):
            flattened.extend(flatten(item))
        else:
            flattened.append(item)
    return flattened
