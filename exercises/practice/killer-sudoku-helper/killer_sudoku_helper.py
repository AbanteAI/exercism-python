def combinations(target, size, exclude):
    def _combinations(target, size, exclude, start):
        if size == 1:
            if target >= start and target <= 9 and target not in exclude:
                return [[target]]
            return []
        result = []
        for i in range(start, 10):
            if i in exclude:
                continue
            sub_combinations = _combinations(target - i, size - 1, exclude, i + 1)
            for sub_combination in sub_combinations:
                result.append([i] + sub_combination)
        return result

    return _combinations(target, size, exclude, 1)