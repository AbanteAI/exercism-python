def best_hands(hands):
    pass
def hand_rank(hand):
    ranks = "23456789TJQKA"
    rank_dict = {r: i for i, r in enumerate(ranks)}
    hand_ranks = sorted([rank_dict[c[0]] for c in hand.split()], reverse=True)
    suits = [c[1] for c in hand.split()]

    flush = len(set(suits)) == 1
    straight = all(hand_ranks[i] - hand_ranks[i+1] == 1 for i in range(len(hand_ranks)-1))

    if straight and flush:
        return 9, hand_ranks
    if any(hand_ranks.count(rank) == 4 for rank in hand_ranks):
        return 8, hand_ranks
    if any(hand_ranks.count(rank) == 3 for rank in hand_ranks) and any(hand_ranks.count(rank) == 2 for rank in hand_ranks):
        return 7, hand_ranks
    if flush:
        return 6, hand_ranks
    if straight:
        return 5, hand_ranks
    if any(hand_ranks.count(rank) == 3 for rank in hand_ranks):
        return 4, hand_ranks
    if any(hand_ranks.count(rank) == 2 for rank in hand_ranks) and len(set(hand_ranks)) == 3:
        return 3, hand_ranks
    if any(hand_ranks.count(rank) == 2 for rank in hand_ranks) and len(set(hand_ranks)) == 4:
        return 2, hand_ranks

    return 1, hand_ranks

def best_hands(hands):
    ranked_hands = [(hand_rank(hand), hand) for hand in hands]
    max_rank = max(ranked_hands, key=lambda x: x[0])[0]
    return [hand for rank, hand in ranked_hands if rank == max_rank]
