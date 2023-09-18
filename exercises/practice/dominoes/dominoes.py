from collections import Counter
def can_chain(dominoes):
    if not dominoes:
        return []

    counts = Counter()
    for domino in dominoes:
        counts[domino[0]] += 1
        counts[domino[1]] += 1

    odd_count = sum(1 for count in counts.values() if count % 2 == 1)

    if odd_count == 0 or odd_count == 2:
        chain = find_chain(dominoes, [], dominoes[0][0])
        return chain if chain else None
    return None

def find_chain(dominoes, chain, start):
    if not dominoes:
        return chain if chain[0][0] == chain[-1][1] else None

    for i, domino in enumerate(dominoes):
        if start in domino:
            flipped = domino[::-1] if domino[0] == start else domino
            new_chain = chain + [flipped]
            remaining_dominoes = dominoes[:i] + dominoes[i+1:]
            result = find_chain(remaining_dominoes, new_chain, flipped[1])
            if result:
                return result
    return None