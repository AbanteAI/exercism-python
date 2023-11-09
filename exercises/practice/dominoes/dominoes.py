def can_chain(dominoes):
    if not dominoes:
        return []

def backtrack(chain, remaining_dominoes):
    if not remaining_dominoes:
        return chain if chain[0][0] == chain[-1][1] else None

    for i, domino in enumerate(remaining_dominoes):
        if not chain or chain[-1][1] == domino[0]:
            result = backtrack(chain + [domino], remaining_dominoes[:i] + remaining_dominoes[i+1:])
            if result:
                return result
        if not chain or chain[-1][1] == domino[1]:
            result = backtrack(chain + [(domino[1], domino[0])], remaining_dominoes[:i] + remaining_dominoes[i+1:])
            if result:
                return result

    return None

return backtrack([], dominoes)