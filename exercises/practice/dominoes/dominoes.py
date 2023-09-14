from itertools import permutations

def can_chain(dominoes):
    if not dominoes:
        return []

    for chain in permutations(dominoes):
        if all(chain[i][1] == chain[i + 1][0] for i in range(len(chain) - 1)):
            if chain[-1][1] == chain[0][0]:
                return chain

    return None