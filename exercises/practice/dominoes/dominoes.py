def can_chain(dominoes):
def can_chain(dominoes):
    if not dominoes:
        return True

    # Helper function to check if two dominoes match
    def match(a, b):
        return a[1] == b[0]

    # Recursive function to try to chain the dominoes
    def search(chain, remaining_dominoes):
        if not remaining_dominoes:
            return chain[0][0] == chain[-1][1]
        for i in range(len(remaining_dominoes)):
            domino = remaining_dominoes[i]
            if match(chain[-1], domino):
                next_chain = chain + [domino]
                next_dominoes = remaining_dominoes[:i] + remaining_dominoes[i+1:]
                if search(next_chain, next_dominoes):
                    return True
            # Also try the flipped domino
            flipped_domino = domino[::-1]
            if match(chain[-1], flipped_domino):
                next_chain = chain + [flipped_domino]
                next_dominoes = remaining_dominoes[:i] + remaining_dominoes[i+1:]
                if search(next_chain, next_dominoes):
                    return True
        return False

    # Start the search with each domino as the starting point
    for i in range(len(dominoes)):
        if search([dominoes[i]], dominoes[:i] + dominoes[i+1:]):
            return True
        if search([dominoes[i][::-1]], dominoes[:i] + dominoes[i+1:]):
            return True

    return False
