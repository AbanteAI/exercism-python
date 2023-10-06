def combinations(target, size, exclude):
    if size == 1:
        if target not in exclude:
            yield [target]
        return

    for i in range(1, target - size + 2):
        if i not in exclude:
            for comb in combinations(target - i, size - 1, exclude + [i]):
                yield [i] + comb
