def combinations(target, size, exclude):
    def backtrack(remaining, start, path):
        if remaining == 0:
            result.append(path)
            return
            if candidates[i] not in path and candidates[i] not in exclude:
                backtrack(remaining - 1, i + 1, path + [candidates[i]])


    candidates = [i for i in range(1, 10) if i not in exclude]
    result = []
    backtrack(size, 0, [])
    return sorted(result)

