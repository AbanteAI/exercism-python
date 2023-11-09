def can_chain(dominoes):
    if not dominoes:
        return []

    # Helper function to check if the chain can be formed starting with the current domino
    def can_chain_from(dominoes, current_chain):
        if not dominoes:
            return current_chain if current_chain[0][0] == current_chain[-1][1] else None

        last_value = current_chain[-1][1]
        for i, domino in enumerate(dominoes):
            if last_value in domino:
                next_domino = (domino if last_value == domino[0] else (domino[1], domino[0]))
                result = can_chain_from(dominoes[:i] + dominoes[i+1:], current_chain + [next_domino])
                if result is not None:
                    return result
        return None

    # Try to start the chain with each domino
    for i, domino in enumerate(dominoes):
        result = can_chain_from(dominoes[:i] + dominoes[i+1:], [domino])
        if result is not None:
            return result
    return None