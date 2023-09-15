from itertools import permutations

def can_chain(dominoes):
    if not dominoes:
        return True

    def is_valid_chain(chain):
        return all(chain[i][-1] == chain[i + 1][0] for i in range(len(chain) - 1)) and chain[-1][-1] == chain[0][0]

    for combination in permutations(dominoes):
        if is_valid_chain(combination):
            return list(combination)

    return None