def best_hands(hands):
    ranks = "23456789TJQKA"
    score = lambda h: (max(h[0], key=h[0].count), sorted(h[0], key=ranks.index, reverse=True))
    return [hand for hand in hands if len(hand) == 5]
    ranks = "23456789TJQKA"
    score = lambda h: (max(h[0], key=h[0].count), sorted(h[0], key=ranks.index, reverse=True))
