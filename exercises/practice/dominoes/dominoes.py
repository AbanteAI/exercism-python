def can_chain(dominoes):
def can_chain(dominoes):
    if not dominoes:
        return []

    def is_valid_chain(chain):
        return all(chain[i][1] == chain[i + 1][0] for i in range(len(chain) - 1))

    def backtrack(chain, remaining_dominoes):
        if not remaining_dominoes:
            if chain[0][0] == chain[-1][1]:
                return chain
            return None

        for i, domino in enumerate(remaining_dominoes):
            new_chain = chain + [domino]
            if is_valid_chain(new_chain):
                result = backtrack(new_chain, remaining_dominoes[:i] + remaining_dominoes[i + 1:])
                if result:
                    return result

            flipped_domino = (domino[1], domino[0])
            new_chain = chain + [flipped_domino]
            if is_valid_chain(new_chain):
                result = backtrack(new_chain, remaining_dominoes[:i] + remaining_dominoes[i + 1:])
                if result:
                    return result

        return None

    return backtrack([], dominoes) or None
