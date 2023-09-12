def best_hands(hands):
from itertools import groupby
from operator import itemgetter
import re
def hand_rank(hand):
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse=True)
    straight = len(set(ranks)) == 5 and max(ranks) - min(ranks) == 4
    flush = len(set(s for r, s in hand)) == 1
    counts = {r: ranks.count(r) for r in set(ranks)}
    groups = sorted([(count, rank) for rank, count in counts.items()], reverse=True)
    return (9 if (5,) == tuple(x[0] for x in groups) and min(ranks) == 1 else
            8 if straight and flush else
            7 if (4, 1) == tuple(x[0] for x in groups) else
            6 if (3, 2) == tuple(x[0] for x in groups) else
            5 if flush else
            4 if straight else
            3 if (3, 1, 1) == tuple(x[0] for x in groups) else
            2 if (2, 2, 1) == tuple(x[0] for x in groups) else
            1 if (2, 1, 1, 1) == tuple(x[0] for x in groups) else
            0), groups

def best_hands(hands):
    return [hand for hand in hands if hand_rank(hand) == max(map(hand_rank, hands))]
