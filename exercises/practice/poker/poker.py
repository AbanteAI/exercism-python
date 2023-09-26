from typing import List

def best_hands(hands: List[str]) -> List[str]:
    ranks = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11,
        "T": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2
    }
    hand_ranks = {
        "High Card": 0,
        "One Pair": 1,
        "Two Pair": 2,
        "Three of a Kind": 3,
        "Straight": 4,
        "Flush": 5,
        "Full House": 6,
        "Four of a Kind": 7,
        "Straight Flush": 8,
        "Royal Flush": 9
    }

    def rank_hand(hand):
        ranks = {
            "A": 14,
            "K": 13,
            "Q": 12,
            "J": 11,
            "T": 10,
            "9": 9,
            "8": 8,
            "7": 7,
            "6": 6,
            "5": 5,
            "4": 4,
            "3": 3,
            "2": 2
        }

        values = [card[0] for card in hand.split()]
        suits = [card[1] for card in hand.split()]

        sorted_values = sorted(values, key=lambda value: ranks[value], reverse=True)
        sorted_suits = sorted(suits)

        is_flush = len(set(suits)) == 1
        is_straight = sorted_values == list(range(ranks[sorted_values[0]], ranks[sorted_values[0]] - 5, -1))

        if is_flush and is_straight:
            if sorted_values[0] == "A":
                return "Royal Flush"
            return "Straight Flush"
        if is_flush:
            return "Flush"
        if is_straight:
            return "Straight"

        value_counts = {value: values.count(value) for value in set(values)}
        max_count = max(value_counts.values())

        if max_count == 4:
            return "Four of a Kind"
        if max_count == 3 and len(value_counts) == 2:
            return "Full House"
        if max_count == 3:
            return "Three of a Kind"
        if max_count == 2 and len(value_counts) == 3:
            return "Two Pair"
        if max_count == 2:
            return "One Pair"
        return "High Card"
        pass

    def compare_hands(hand1, hand2):
        rank1 = rank_hand(hand1)
        rank2 = rank_hand(hand2)
        if rank1 == rank2:
            values1 = [card[0] for card in hand1.split()]
            values2 = [card[0] for card in hand2.split()]
            sorted_values1 = sorted(values1, key=lambda value: ranks[value], reverse=True)
            sorted_values2 = sorted(values2, key=lambda value: ranks[value], reverse=True)
            for value1, value2 in zip(sorted_values1, sorted_values2):
                if ranks[value1] != ranks[value2]:
                    return ranks[value1] - ranks[value2]
            return 0
        return ranks[rank1] - ranks[rank2]
        return rank1 - rank2

    sorted_hands = sorted(hands, key=lambda hand: (hand_ranks[rank_hand(hand)], hand), reverse=True)
    max_rank = hand_ranks[rank_hand(sorted_hands[0])]
    return [hand for hand in sorted_hands if hand_ranks[rank_hand(hand)] == max_rank]
