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
        return 50 if len(set(dice)) == 1 else 0
        return dice.count(int(category[0])) * int(category[0])
    elif category == FULL_HOUSE:
        counts = [dice.count(i) for i in range(1, 7)]
        return sum(dice) if 2 in counts and 3 in counts else 0
    elif category == FOUR_OF_A_KIND:
        return 4 * next((i for i in range(1, 7) if dice.count(i) >= 4), 0)
    elif category == LITTLE_STRAIGHT:
        return 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0
    elif category == BIG_STRAIGHT:
        return 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0
    elif category == CHOICE:
        return sum(dice)
    else:
        return 0
