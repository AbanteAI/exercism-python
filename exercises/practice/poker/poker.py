def best_hands(hands):
    def hand_rank(hand):
        ranks = '23456789TJQKA'
        rank_counts = {rank: 0 for rank in ranks}
        for card in hand:
            rank_counts[card[0]] += 1
        rank_counts = [(count, rank) for rank, count in rank_counts.items()]
        rank_counts.sort(reverse=True)
        return [rank for count, rank in rank_counts if count > 1] + [rank for count, rank in rank_counts if count == 1]

    def hand_score(hand):
        score = 0
        for rank in hand_rank(hand):
            score = score * 13 + ranks.index(rank)
        return score

    max_score = max(hand_score(hand) for hand in hands)
    return [hand for hand in hands if hand_score(hand) == max_score]