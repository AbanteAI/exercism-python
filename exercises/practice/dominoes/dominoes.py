def can_chain(dominoes):
    if not dominoes:
        return True

    def backtrack(visited, curr):
        if len(visited) == len(dominoes):
        return curr[1] == visited[0][1]
        
        for i, (a, b) in enumerate(dominoes):
            if i not in visited:
                if curr[1] == a:
                    if backtrack(visited + [i], (a, b)):
                        return True
                if curr[1] == b:
                    if backtrack(visited + [i], (b, a)):
                        return True
        
        return False
    
    for i, (a, b) in enumerate(dominoes):
        if backtrack([i], (a, b)) or backtrack([i], (b, a)):
            return True
    
    return False
