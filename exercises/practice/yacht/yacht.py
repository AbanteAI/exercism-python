# Score categories.
# Change the values as you see fit.
def digits(num):
    return lambda dice: dice.count(num) * num

YACHT = lambda dice: 50 if len(set(dice)) == 1 else 0
ONES = digits(1)
TWOS = digits(2)
THREES = digits(3)
FOURS = digits(4)
FIVES = digits(5)
SIXES = digits(6)
FULL_HOUSE = lambda dice: sum(dice) if len(set(dice)) == 2 and dice.count(dice[0]) in [2, 3] else 0
FOUR_OF_A_KIND = lambda dice: 4 * sorted(dice)[1] if len(set(dice)) < 3 and dice.count(dice[0]) in (1, 4, 5) else 0
LITTLE_STRAIGHT = lambda dice: 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0
BIG_STRAIGHT = lambda dice: 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0
CHOICE = sum


def score(dice, category):
    return category(dice)