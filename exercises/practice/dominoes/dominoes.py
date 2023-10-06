def can_chain(dominoes):
    if not dominoes:
        return True

    def backtrack(chain, remaining):
        if not remaining:
            return chain[0][0] == chain[-1][1]

        for i, domino in enumerate(remaining):
            if chain[-1][1] == domino[0]:
                result = backtrack(chain + [domino], remaining[:i] + remaining[i+1:])
                if result:
                    return True
            if chain[-1][1] == domino[1]:
                result = backtrack(chain + [(domino[1], domino[0])], remaining[:i] + remaining[i+1:])
                if result:
                    return True

        return False

    return backtrack([dominoes[0]], dominoes[1:])
