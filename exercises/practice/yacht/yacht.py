# Score categories.
# Change the values as you see fit.
YACHT = lambda dice: 50 if len(set(dice)) == 1 else 0
ONES = lambda dice: sum(d for d in dice if d == 1) * 1
TWOS = lambda dice: sum(d for d in dice if d == 2) * 2
THREES = lambda dice: sum(d for d in dice if d == 3) * 3
FOURS = lambda dice: sum(d for d in dice if d == 4) * 4
FIVES = lambda dice: sum(d for d in dice if d == 5) * 5
SIXES = lambda dice: sum(d for d in dice if d == 6) * 6
FULL_HOUSE = lambda dice: sum(dice) if len(set(dice)) == 2 and any(dice.count(x) == 3 for x in set(dice)) else 0
FOUR_OF_A_KIND = lambda dice: sum(x * 4 for x in set(dice) if dice.count(x) >= 4)
LITTLE_STRAIGHT = lambda dice: 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0
BIG_STRAIGHT = lambda dice: 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0
CHOICE = lambda dice: sum(dice)


def score(dice, category):
    return category(dice)
