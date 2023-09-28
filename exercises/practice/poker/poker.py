def best_hands(hands):
    pass
def hand_value(hand):
    values = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14,
    }
    suits = 'CDHS'
    card_ranks = sorted([values[card[:-1]] for card in hand.split()], reverse=True)
    card_suits = [card[-1] for card in hand.split()]
    flush = len(set(card_suits)) == 1
    straight = all(card_ranks[i] - card_ranks[i + 1] == 1 for i in range(4))

    if flush and straight:
        return (8, card_ranks)
    if any(card_ranks.count(rank) == 4 for rank in card_ranks):
        return (7, [rank for rank in card_ranks if card_ranks.count(rank) == 4][0])
    if any(card_ranks.count(rank) == 3 for rank in card_ranks) and any(card_ranks.count(rank) == 2 for rank in card_ranks):
        return (6, [rank for rank in card_ranks if card_ranks.count(rank) == 3][0])
    if flush:
        return (5, card_ranks)
    if straight:
        return (4, card_ranks)
    if any(card_ranks.count(rank) == 3 for rank in card_ranks):
        return (3, [rank for rank in card_ranks if card_ranks.count(rank) == 3][0])
    if any(card_ranks.count(rank) == 2 for rank in card_ranks) and sum(card_ranks.count(rank) == 2 for rank in card_ranks) == 4:
        return (2, sorted([rank for rank in card_ranks if card_ranks.count(rank) == 2], reverse=True))
    if any(card_ranks.count(rank) == 2 for rank in card_ranks):
        return (1, [rank for rank in card_ranks if card_ranks.count(rank) == 2][0])
    return (0, card_ranks)

def best_hands(hands):
    hand_values = [(hand, hand_value(hand)) for hand in hands]
    max_value = max(hand_values, key=lambda x: x[1])[1]
    return [hand for hand, value in hand_values if value == max_value]
