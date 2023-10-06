def best_hands(hands):
def hand_rank(hand):
    """Return a tuple representing the rank of a hand."""
    ranks = ['--23456789TJQKA'.index(c) for c, s in hand]
    ranks.sort(reverse=True)
    if ranks == [14, 5, 4, 3, 2]:
        return (5, [5, 4, 3, 2, 1])
    straight = len(set(ranks)) == 5 and max(ranks) - min(ranks) == 4
    flush = len(set(s for c, s in hand)) == 1
    counts = {ranks.count(r): r for r in ranks}
    if straight and flush:
        return (9 if ranks[0] == 14 else 8, ranks)
    if 4 in counts:
        return (7, [counts[4], counts[1]])
    if 3 in counts and 2 in counts:
        return (6, [counts[3], counts[2]])
    if flush:
        return (5, ranks)
    if straight:
        return (4, ranks)
    if 3 in counts:
        return (3, [counts[3]] + sorted([r for r in ranks if r != counts[3]], reverse=True))
    if 2 in counts and len(counts) == 3:
        return (2, [counts[2], counts[2], counts[1]])
    if 2 in counts:
        return (1, [counts[2]] + sorted([r for r in ranks if r != counts[2]], reverse=True))
    return (0, ranks)

def best_hands(hands):
    ranked_hands = [(hand_rank(hand), hand) for hand in hands]
    max_rank = max(ranked_hands, key=lambda x: x[0])[0]
    return [hand for rank, hand in ranked_hands if rank == max_rank]
