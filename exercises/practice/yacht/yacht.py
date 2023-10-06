# Score categories.
# Change the values as you see fit.
YACHT = None
ONES = None
TWOS = None
THREES = None
FOURS = None
FIVES = None
SIXES = None
FULL_HOUSE = None
FOUR_OF_A_KIND = None
LITTLE_STRAIGHT = None
BIG_STRAIGHT = None
CHOICE = None


def score(dice, category):
    if category == "YACHT":
        return 50 if len(set(dice)) == 1 else 0
    elif category == "ONES":
        return dice.count(1)
    elif category == "TWOS":
        return dice.count(2) * 2
    elif category == "THREES":
        return dice.count(3) * 3
    elif category == "FOURS":
        return dice.count(4) * 4
    elif category == "FIVES":
        return dice.count(5) * 5
    elif category == "SIXES":
        return dice.count(6) * 6
    elif category == "FULL_HOUSE":
        counts = set(dice)
        if len(counts) == 2 and (dice.count(d) == 2 or dice.count(d) == 3 for d in counts):
            return sum(dice)
        return 0
    elif category == "FOUR_OF_A_KIND":
        for d in set(dice):
            if dice.count(d) >= 4:
                return 4 * d
        return 0
    elif category == "LITTLE_STRAIGHT":
        return 30 if set(dice) == {1, 2, 3, 4, 5} else 0
    elif category == "BIG_STRAIGHT":
        return 30 if set(dice) == {2, 3, 4, 5, 6} else 0
    elif category == "CHOICE":
        return sum(dice)
    else:
        return 0
