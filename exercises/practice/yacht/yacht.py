# Score categories.
# Change the values as you see fit.
YACHT = 50
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
    if category == YACHT:
        if len(set(dice)) == 1:
            return 50
    elif category == ONES:
        return dice.count(1) * 1
    elif category == TWOS:
        return dice.count(2) * 2
    elif category == THREES:
        return dice.count(3) * 3
    elif category == FOURS:
        return dice.count(4) * 4
    elif category == FIVES:
        return dice.count(5) * 5
    elif category == SIXES:
        return dice.count(6) * 6
    elif category == FULL_HOUSE:
        unique_dice = set(dice)
        if len(unique_dice) == 2 and all(dice.count(die) == 3 or dice.count(die) == 2 for die in unique_dice):
            return sum(dice)
    elif category == FOUR_OF_A_KIND:
        for die in set(dice):
            if dice.count(die) >= 4:
                return die * 4
    elif category == LITTLE_STRAIGHT:
        if sorted(dice) == [1, 2, 3, 4, 5]:
            return 30
    elif category == BIG_STRAIGHT:
        if sorted(dice) == [2, 3, 4, 5, 6]:
            return 30
    elif category == CHOICE:
        return sum(dice)
    return 0
