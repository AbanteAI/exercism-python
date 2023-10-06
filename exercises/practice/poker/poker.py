def best_hands(hands):
    def parse_hand(hand):
        ranks = "23456789TJQKA"
        suits = "CDHS"
        return [(ranks.index(card[0]), suits.index(card[1])) for card in hand.split()]

    def is_straight_flush(hand):
        return is_flush(hand) and is_straight(hand)

    def is_four_of_a_kind(hand):
        ranks = [card[0] for card in hand]
        return any(ranks.count(rank) == 4 for rank in ranks)

    def is_full_house(hand):
        ranks = [card[0] for card in hand]
        return sorted(set(ranks), key=lambda x: ranks.count(x), reverse=True) == [3, 2]

    def is_flush(hand):
        return all(card[1] == hand[0][1] for card in hand)

    def is_straight(hand):
        ranks = sorted(card[0] for card in hand)
        return ranks == list(range(ranks[0], ranks[0] + 5))

    def is_three_of_a_kind(hand):
        ranks = [card[0] for card in hand]
        return any(ranks.count(rank) == 3 for rank in ranks)

    def is_two_pair(hand):
        ranks = [card[0] for card in hand]
        return sorted(set(ranks), key=lambda x: ranks.count(x), reverse=True) == [2, 2]

    def is_one_pair(hand):
        ranks = [card[0] for card in hand]
        return any(ranks.count(rank) == 2 for rank in ranks)

    def rank_hand(hand):
        if is_straight_flush(hand):
            return 8
        if is_four_of_a_kind(hand):
            return 7
        if is_full_house(hand):
            return 6
        if is_flush(hand):
            return 5
        if is_straight(hand):
            return 4
        if is_three_of_a_kind(hand):
            return 3
        if is_two_pair(hand):
            return 2
        if is_one_pair(hand):
            return 1
        return 0

    hands = [parse_hand(hand) for hand in hands]
    max_rank = max(rank_hand(hand) for hand in hands)
    return [hand for hand in hands if rank_hand(hand) == max_rank]

