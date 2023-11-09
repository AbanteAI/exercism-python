from itertools import permutations

from itertools import permutations

def solve_puzzle():
    # There are five houses
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(permutations(houses))  # 1
    nationalities = {1: "Norwegian", 2: "Ukrainian", 3: "Englishman", 4: "Spaniard", 5: "Japanese"}
    return next(((nationalities[WATER], nationalities[ZEBRA]))
                for (red, green, ivory, yellow, blue) in orderings
                if imright(green, ivory)  # 6
                for (Englishman, Spaniard, Ukrainian, Japanese, Norwegian) in orderings
                if Englishman is red  # 2
                if Norwegian is first  # 10
                if nextto(Norwegian, blue)  # 15
                for (coffee, tea, milk, oj, WATER) in orderings
                if coffee is green  # 4
                if Ukrainian is tea  # 5
                if milk is middle  # 9
                for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
                if Kools is yellow  # 8
                if LuckyStrike is oj  # 13
                if Japanese is Parliaments  # 14
                for (dog, snails, fox, horse, ZEBRA) in orderings
                if Spaniard is dog  # 3
                if OldGold is snails  # 7
                if nextto(Chesterfields, fox)  # 11
                if nextto(Kools, horse)  # 12
                )

def imright(h1, h2):
    "House h1 is immediately to the right of h2."
    return h1 - h2 == 1

def nextto(h1, h2):
    "Two houses are next to each other."
    return abs(h1 - h2) == 1

def drinks_water():
    "Return the nationality of the resident who drinks water."
    water_drinker, _ = solve_puzzle()
    return water_drinker

def owns_zebra():
    "Return the nationality of the resident who owns the zebra."
    _, zebra_owner = solve_puzzle()
    return zebra_owner