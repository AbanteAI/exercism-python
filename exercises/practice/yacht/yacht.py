# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    counts = [dice.count(i) for i in range(1, 7)]
    if category == YACHT and 5 in counts:
        return 50
    elif category in [ONES, TWOS, THREES, FOURS, FIVES, SIXES]:
        return counts[category - 1] * (category - 1)
    elif category == FULL_HOUSE and sorted(counts) == [2, 3]:
        return sum(dice)
    elif category == FOUR_OF_A_KIND and (4 in counts or 5 in counts):
        return 4 * next(i for i, count in enumerate(counts) if count >= 4)
    elif category == LITTLE_STRAIGHT and sorted(dice) == [1, 2, 3, 4, 5]:
        return 30
    elif category == BIG_STRAIGHT and sorted(dice) == [2, 3, 4, 5, 6]:
        return 30
    elif category == CHOICE:
        return sum(dice)
    else:
        return 0


def score(dice, category):
    pass
