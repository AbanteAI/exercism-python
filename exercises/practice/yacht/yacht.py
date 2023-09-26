# Score categories.
# Change the values as you see fit.
YACHT = "Yacht"
ONES = "Ones"
TWOS = "Twos"
THREES = "Threes"
FOURS = "Fours"
FIVES = "Fives"
SIXES = "Sixes"
FULL_HOUSE = "Full House"
FOUR_OF_A_KIND = "Four of a Kind"
LITTLE_STRAIGHT = "Little Straight"
BIG_STRAIGHT = "Big Straight"
CHOICE = "Choice"

def score(dice, category):
    if category == ONES:
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
        if len(set(dice)) == 2 and (dice.count(dice[0]) == 2 or dice.count(dice[0]) == 3):
            return sum(dice)
        else:
            return 0
    elif category == FOUR_OF_A_KIND:
        for num in set(dice):
            if dice.count(num) >= 4:
                return num * 4
        return 0
    elif category == LITTLE_STRAIGHT:
        if set(dice) == {1, 2, 3, 4, 5}:
            return 30
        else:
            return 0
    elif category == BIG_STRAIGHT:
       


def score(dice, category):
    if category == "Ones":
        return dice.count(1) * 1
    elif category == "Twos":
        return dice.count(2) * 2
    elif category == "Threes":
        return dice.count(3) * 3
    elif category == "Fours":
        return dice.count(4) * 4
    elif category == "Fives":
        return dice.count(5) * 5
    elif category == "Sixes":
        return dice.count(6) * 6
    elif category == "Full House":
        if len(set(dice)) == 2 and (dice.count(dice[0]) == 2 or dice.count(dice[0]) == 3):
            return sum(dice)
        else:
            return 0
    elif category == "Four of a Kind":
        for num in set(dice):
            if dice.count(num) >= 4:
                return num * 4
        return 0
    elif category == "Little Straight":
        if set(dice) == {1, 2, 3, 4, 5}:
            return 30
        else:
            return 0
    elif category == "Big Straight":
        if set(dice) == {2, 3, 4, 5, 6}:
            return 30
        else:
            return 0
    elif category == "Choice":
        return sum(dice)
    elif category == "Yacht":
        if len(set(dice)) == 1:
            return 50
        else:
            return 0
    else:
        return 0
