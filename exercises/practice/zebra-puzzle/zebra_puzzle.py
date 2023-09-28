from itertools import permutations

def generate_permutations(items):
    return list(permutations(items))

def is_valid(arrangement):
    (red, green, ivory, yellow, blue) = arrangement[0]
    (Englishman, Spaniard, Ukrainian, Norwegian, Japanese) = arrangement[1]
    (dog, snails, fox, horse, zebra) = arrangement[2]
    (coffee, tea, milk, orange_juice, water) = arrangement[3]
    (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) = arrangement[4]

    return (
        Englishman == red and
        Spaniard == dog and
        coffee == green and
        Ukrainian == tea and
        green == ivory + 1 and
        OldGold == snails and
        Kools == yellow and
        milk == 3 and
        Norwegian == 1 and
        abs(Chesterfields - fox) == 1 and
        abs(Kools - horse) == 1 and
        LuckyStrike == orange_juice and
        Japanese == Parliaments and
        abs(Norwegian - blue) == 1
    )

from itertools import product

def solve_puzzle():
    houses = [1, 2, 3, 4, 5]
    arrangements = product(generate_permutations(houses), repeat=5)
    for arrangement in arrangements:
        if is_valid(arrangement):
            return arrangement

solution = solve_puzzle()

def drinks_water():
    (_, _, _, _, water_drinker) = solution[3]
    return water_drinker

def owns_zebra():
    (_, _, _, _, zebra_owner) = solution[2]
    return zebra_owner
from itertools import permutations

def generate_permutations(items):
    return list(permutations(items))

def is_valid(arrangement):
    (red, green, ivory, yellow, blue) = arrangement[0]
    (Englishman, Spaniard, Ukrainian, Norwegian, Japanese) = arrangement[1]
    (dog, snails, fox, horse, zebra) = arrangement[2]
    (coffee, tea, milk, orange_juice, water) = arrangement[3]
    (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) = arrangement[4]

    return (
        Englishman == red and
        Spaniard == dog and
        coffee == green and
        Ukrainian == tea and
        green == ivory + 1 and
        OldGold == snails and
        Kools == yellow and
        milk == 3 and
        Norwegian == 1 and
        abs(Chesterfields - fox) == 1 and
        abs(Kools - horse) == 1 and
        LuckyStrike == orange_juice and
        Japanese == Parliaments and
        abs(Norwegian - blue) == 1
    )

def solve_puzzle():
    houses = [1, 2, 3, 4, 5]
    arrangements = generate_permutations(houses)
    for arrangement in arrangements:
        if is_valid(arrangement):
            return arrangement

solution = solve_puzzle()

def drinks_water():
    (_, _, _, _, water_drinker) = solution[3]
    return water_drinker

def owns_zebra():
    (_, _, _, _, zebra_owner) = solution[2]
    return zebra_owner
    pass


def owns_zebra():
    pass
