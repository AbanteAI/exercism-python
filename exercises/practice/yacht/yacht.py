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
    dice_count = [dice.count(i) for i in range(1, 7)]

    category_to_number = {
        ONES: 1,
        TWOS: 2,
        THREES: 3,
        FOURS: 4,
        FIVES: 5,
        SIXES: 6
    }
    if category in [ONES, TWOS, THREES, FOURS, FIVES, SIXES]:
        return (category_to_number[category] * dice_count[category_to_number[category] - 1])
        if 2 in dice_count and 3 in dice_count:
            return sum(dice)
        else:
            return 0
        if dice_count.count(4) > 0:
        if dice_count.count(4) > 0:
            return 4 * (dice_count.index(4) + 1)
        else:
            return 0
        return 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0
    elif category == BIG_STRAIGHT:
        return 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0
    elif category == CHOICE:
        return sum(dice)
    elif category == YACHT:
        return 50 if len(set(dice)) == 1 else 0
    else:
        return 0
