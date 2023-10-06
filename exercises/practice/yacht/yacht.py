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
    dice_counts = [dice.count(i) for i in range(1, 7)]
    
        return dice_counts[int(category[-1]) - 1] * int(category[-1])
    elif category == FULL_HOUSE:
        if 2 in dice_counts and 3 in dice_counts:
            return sum(dice)
        return 0
    elif category == FOUR_OF_A_KIND:
            return (dice_counts.index(4) + 1) * 4
        return 0
    elif category == LITTLE_STRAIGHT:
        return 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0
    elif category == BIG_STRAIGHT:
        return 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0
    elif category == CHOICE:
        return sum(dice)
    elif category == YACHT:
        return 50 if len(set(dice)) == 1 else 0
    return 0