# Score categories.
# Change the values as you see fit.
YACHT = "YACHT"
ONES = "ONES"
TWOS = "TWOS"
THREES = "THREES"
FOURS = "FOURS"
FIVES = "FIVES"
SIXES = "SIXES"
FULL_HOUSE = "FULL_HOUSE"
FOUR_OF_A_KIND = "FOUR_OF_A_KIND"
LITTLE_STRAIGHT = "LITTLE_STRAIGHT"
BIG_STRAIGHT = "BIG_STRAIGHT"
CHOICE = "CHOICE"

def score(dice, category):
    if category == YACHT:
        return 50 if len(set(dice)) == 1 else 0
    elif category == ONES:
        return dice.count(1)
    elif category == TWOS:
        return 2 * dice.count(2)
    elif category == THREES:
        return 3 * dice.count(3)
    elif category == FOURS:
        return 4 * dice.count(4)
    elif category == FIVES:
        return 5 * dice.count(5)
    elif category == SIXES:
        return 6 * dice.count(6)
    elif category == FULL_HOUSE:
        counts = set(dice)
        if len(counts) != 2 or (dice.count(counts.pop()) != 2 and dice.count(counts.pop()) != 3):
            return 0
        return sum(dice)
    elif category == FOUR_OF_A_KIND:
        for value in set(dice):
            if dice.count(value) >= 4:
                return 4 * value
        return 0
    elif category == LITTLE_STRAIGHT:
        return 30 if set(dice) == {1, 2, 3, 4, 5} else 0
    elif category == BIG_STRAIGHT:
        return 30 if set(dice) == {2, 3, 4, 5, 6} else 0
    elif category == CHOICE:
        return sum(dice)
    else:
        return 0


def score(dice, category):
    if category == YACHT:
        return 50 if len(set(dice)) == 1 else 0
    elif category == ONES:
        return dice.count(1)
    elif category == TWOS:
        return 2 * dice.count(2)
    elif category == THREES:
        return 3 * dice.count(3)
    elif category == FOURS:
        return 4 * dice.count(4)
    elif category == FIVES:
        return 5 * dice.count(5)
    elif category == SIXES:
        return 6 * dice.count(6)
    elif category == FULL_HOUSE:
        counts = set(dice)
        if len(counts) != 2 or (dice.count(counts.pop()) != 2 and dice.count(counts.pop()) != 3):
            return 0
        return sum(dice)
    elif category == FOUR_OF_A_KIND:
        for value in set(dice):
            if dice.count(value) >= 4:
                return 4 * value
        return 0
    elif category == LITTLE_STRAIGHT:
        return 30 if set(dice) == {1, 2, 3, 4, 5} else 0
    elif category == BIG_STRAIGHT:
        return 30 if set(dice) == {2, 3, 4, 5, 6} else 0
    elif category == CHOICE:
        return sum(dice)
    else:
        return 0
