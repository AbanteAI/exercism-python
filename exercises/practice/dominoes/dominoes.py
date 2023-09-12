def can_chain(dominoes):
    if not dominoes:
        return []
    
    def is_chainable(dominoes):
        degree = {}
        for d in dominoes:
            degree[d[0]] = degree.get(d[0], 0) + 1
            degree[d[1]] = degree.get(d[1], 0) + 1
        odd_degrees = [d for d in degree.values() if d % 2 == 1]
        return len(odd_degrees) == 0 or len(odd_degrees) == 2

    def dfs(path, remaining):
        if not remaining:
            if path[0][0] == path[-1][1]:
                return path
            return None
        for i, domino in enumerate(remaining):
            if path[-1][1] in domino:
                new_remaining = remaining[:i] + remaining[i+1:]
                if domino[0] != path[-1][1]:
                    domino = (domino[1], domino[0])
                new_path = dfs(path + [domino], new_remaining)
                if new_path:
                    return new_path
        return None

    if not is_chainable(dominoes):
        return None

    return dfs([dominoes[0]], dominoes[1:])