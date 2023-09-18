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
    dice_counts = [dice.count(i) for i in range(1, 7)]

    if category == ONES:
        return dice_counts[0]
    elif category == TWOS:
        return dice_counts[1] * 2
    elif category == THREES:
        return dice_counts[2] * 3
    elif category == FOURS:
        return dice_counts[3] * 4
    elif category == FIVES:
        return dice_counts[4] * 5
    elif category == SIXES:
        return dice_counts[5] * 6
    elif category == FULL_HOUSE:
        if 2 in dice_counts and 3 in dice_counts:
            return sum(dice)
        else:
            return 0
    elif category == FOUR_OF_A_KIND:
        if 4 in dice_counts or 5 in dice_counts:
            if 5 in dice_counts:
                return dice_counts.index(5) * 4
            else:
                return dice_counts.index(4) * 4
    elif category == LITTLE_STRAIGHT:
        return 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0
    elif category == BIG_STRAIGHT:
        return 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0
    elif category == CHOICE:
        return sum(dice)
    elif category == YACHT:
        return 50 if len(set(dice)) == 1 else 0
    else:
        return 0
