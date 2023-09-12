def combinations(target, size, exclude):
    def helper(start, target, size, path, exclude):
        if target == 0 and size == 0:
            return [path]
        if target < 0 or size == 0:
            return []
        result = []
        for i in range(start, 10):
            if i not in exclude:
                result.extend(helper(i + 1, target - i, size - 1, path + [i], exclude))
        return result

    return helper(1, target, size, [], exclude)