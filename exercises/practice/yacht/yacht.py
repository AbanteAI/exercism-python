# Score categories.
# Change the values as you see fit.
YACHT = lambda dice: 50 if len(set(dice)) == 1 else 0
ONES = lambda dice: sum(die for die in dice if die == 1)
TWOS = lambda dice: sum(die for die in dice if die == 2)
THREES = lambda dice: sum(die for die in dice if die == 3)
FOURS = lambda dice: sum(die for die in dice if die == 4)
FIVES = lambda dice: sum(die for die in dice if die == 5)
SIXES = lambda dice: sum(die for die in dice if die == 6)
FULL_HOUSE = lambda dice: sum(dice) if sorted(dice.count(die) for die in set(dice)) == [2, 3] else 0
FOUR_OF_A_KIND = lambda dice: 4 * next((die for die in set(dice) if dice.count(die) >= 4), 0)
LITTLE_STRAIGHT = lambda dice: 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0
BIG_STRAIGHT = lambda dice: 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0
CHOICE = sum


def score(dice, category):
    return category(dice)
