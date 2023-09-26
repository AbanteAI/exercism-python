def keep(sequence, predicate):
    return [x for x in sequence if predicate(x)]
    pass


def discard(sequence, predicate):
    return [x for x in sequence if not predicate(x)]
    pass
