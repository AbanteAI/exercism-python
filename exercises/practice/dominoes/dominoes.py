def can_chain(dominoes):
    if not dominoes:
        return []

    # Create a copy of the dominoes list to avoid modifying the original list
    dominoes = dominoes[:]

    def search(chain, remaining_dominoes):
        if not remaining_dominoes and chain[0][0] == chain[-1][1]:
            return chain
        for i, domino in enumerate(remaining_dominoes):
            if chain[-1][1] == domino[0]:
                new_chain = search(chain + [domino], remaining_dominoes[:i] + remaining_dominoes[i+1:])
                if new_chain:
                    return new_chain
            elif chain[-1][1] == domino[1]:
                new_chain = search(chain + [domino[::-1]], remaining_dominoes[:i] + remaining_dominoes[i+1:])
                if new_chain:
                    return new_chain
        return None

    for i, domino in enumerate(dominoes):
        chain = search([domino], dominoes[:i] + dominoes[i+1:])
        if chain:
            return chain
    return None