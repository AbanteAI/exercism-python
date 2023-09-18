def combinations(target, size, exclude):
    def _combinations(current_sum, current_size, start):
        if current_size == size:
            if current_sum == target:
                return [[]]
            else:
                return []

        result = []
        for i in range(start, 10):
            if i not in exclude:
                sub_combinations = _combinations(current_sum + i, current_size + 1, i + 1)
                for sub_combination in sub_combinations:
                    result.append([i] + sub_combination)
        return result

    return _combinations(0, 0, 1)