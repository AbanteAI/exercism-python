def can_chain(dominoes):
    pass
def can_add_to_chain(chain, domino):
    return (chain[-1][1] == domino[0] and chain[0][0] == domino[1]) or (chain[-1][1] == domino[1] and chain[0][0] == domino[0])

def find_chains(dominoes, chain=None):
    if chain is None:
        chain = []

    if not dominoes:
        if can_add_to_chain(chain, chain[0]):
            return [chain]
        return []

    chains = []
    for i, domino in enumerate(dominoes):
        if can_add_to_chain(chain, domino):
            new_dominoes = dominoes[:i] + dominoes[i + 1:]
            new_chain = chain + [domino if chain[-1][1] == domino[0] else (domino[1], domino[0])]
            chains.extend(find_chains(new_dominoes, new_chain))
        else:
            reversed_domino = (domino[1], domino[0])
            if can_add_to_chain(chain, reversed_domino):
                new_dominoes = dominoes[:i] + dominoes[i + 1:]
                new_chain = chain + [reversed_domino]
                chains.extend(find_chains(new_dominoes, new_chain))

    return chains

def can_chain(dominoes):
    if not dominoes:
        return []

    for i, domino in enumerate(dominoes):
        chains = find_chains(dominoes[:i] + dominoes[i + 1:], [domino])
        if chains:
            return chains[0]

    return None
