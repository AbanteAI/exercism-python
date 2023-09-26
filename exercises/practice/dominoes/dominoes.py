def can_chain(dominoes):
    if len(dominoes) == 0:
        return True

    def backtrack(chain, remaining):
        if len(remaining) == 0:
            return chain[0][0] == chain[-1][1]

        last = chain[-1][1]
        for i, domino in enumerate(remaining):
            if last in domino:
                new_chain = chain + [domino]
                new_remaining = remaining[:i] + remaining[i + 1:]
                if backtrack(new_chain, new_remaining):
                    return True
        return False

    return backtrack([dominoes[0]], dominoes[1:])
        return True

    def backtrack(chain, remaining):
        if len(remaining) == 0:
            return chain[0][0] == chain[-1][1]

        last = chain[-1][1]
        for i, domino in enumerate(remaining):
            if last in domino:
                new_chain = chain + [domino]
                new_remaining = remaining[:i] + remaining[i + 1:]
                if backtrack(new_chain, new_remaining):
                    return True
        return False

    return backtrack([dominoes[0]], dominoes[1:])
