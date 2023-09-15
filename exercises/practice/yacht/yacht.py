# Score categories.
# Change the values as you see fit.
YACHT = "yacht"
ONES = "ones"
TWOS = "twos"
THREES = "threes"
FOURS = "fours"
FIVES = "fives"
SIXES = "sixes"
FULL_HOUSE = "full_house"
FOUR_OF_A_KIND = "four_of_a_kind"
LITTLE_STRAIGHT = "little_straight"
BIG_STRAIGHT = "big_straight"
CHOICE = "choice"

def score(dice, category):
    if category == YACHT:
        if len(set(dice)) == 1:
            return 50
        else:
            return 0
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
        if len(set(dice)) == 2 and dice.count(dice[0]) in [2, 3]:
            return sum(dice)
        else:
            return 0
    elif category == FOUR_OF_A_KIND:
        for num in set(dice):
            if dice.count(num) >= 4:
                return 4 * num
        return 0
    elif category == LITTLE_STRAIGHT:
        if set(dice) == {1, 2, 3, 4, 5}:
            return 30
        else:
            return 0
   


def score(dice, category):
    pass
