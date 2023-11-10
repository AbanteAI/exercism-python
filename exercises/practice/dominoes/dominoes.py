def can_chain(dominoes):
    if not dominoes:
        return None

    # Helper function to check if two dominoes match
    def match(a, b):
        return a[1] == b[0]

    # Helper function to attempt to build a chain
    def build_chain(chain, remaining):
        if not remaining:
            return chain[0][0] == chain[-1][1] and chain or None

        for i, domino in enumerate(remaining):
            if match(chain[-1], domino):
                new_chain = chain + [domino]
                new_remaining = remaining[:i] + remaining[i+1:]
                result = build_chain(new_chain, new_remaining)
                if result:
                    return result
            # Also try with flipped domino
            flipped_domino = domino[::-1]
            if match(chain[-1], flipped_domino):
                new_chain = chain + [flipped_domino]
                new_remaining = remaining[:i] + remaining[i+1:]
                result = build_chain(new_chain, new_remaining)
                if result:
                    return result
        return None

    # Start the chain with each domino and try to build from there
    for i, domino in enumerate(dominoes):
        remaining = dominoes[:i] + dominoes[i+1:]
        chain = build_chain([domino], remaining)
        if chain:
            return chain
        # Also try with the domino flipped
        chain = build_chain([domino[::-1]], remaining)
        if chain:
            return chain

    return None