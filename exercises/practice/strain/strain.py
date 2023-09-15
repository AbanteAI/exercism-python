def keep(sequence, predicate):
    result = []
    for item in sequence:
        if predicate(item):
            result.append(item)
    return result


def discard(sequence, predicate):
    result = []
    for item in sequence:
        if not predicate(item):
            result.append(item)
    return result
