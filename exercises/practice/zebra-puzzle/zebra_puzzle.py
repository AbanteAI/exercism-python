

def owns_zebra():
    pass

from itertools import permutations

def all_permutations(items):
    return list(permutations(items))

def solve_zebra_puzzle():
    houses = list(range(1, 6))
    orderings = list(all_permutations(houses))
    for (red, green, ivory, yellow, blue) in orderings:
        if green != ivory + 1:
            continue
        for (Englishman, Spaniard, Ukrainian, Norwegian, Japanese) in orderings:
            if Norwegian != 1:
                continue
            if Englishman != red:
                continue
            if blue != Norwegian - 1 and blue != Norwegian + 1:
            for (dog, snails, fox, horse, zebra) in orderings:
                if Spaniard != dog:
                    continue
                for (coffee, tea, milk, orange_juice, water) in orderings:
                    if coffee != green:
                        continue
                    if Ukrainian != tea:
                        continue
                    if milk != 3:
                        continue
                    for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings:
                        if OldGold != snails:
                            continue
                        if Kools != yellow:
                            continue
                        if Chesterfields != fox - 1 and Chesterfields != fox + 1:
                            continue
                        if Kools != horse - 1 and Kools != horse + 1:
                            continue
                        if LuckyStrike != orange_juice:
                            continue
                        if Japanese != Parliaments:
                            continue
                        return (houses, Englishman, Spaniard, Ukrainian, Norwegian, Japanese, red, green, ivory, yellow, blue, dog, snails, fox, horse, zebra, coffee, tea, milk, orange_juice, water, OldGold, Kools, Chesterfields, LuckyStrike, Parliaments)

def drinks_water():
    (_, Englishman, Spaniard, Ukrainian, Norwegian, Japanese, _, _, _, _, _, _, _, _, _, _, _, _, _, water, _, _, _, _, _, _) = solve_zebra_puzzle()
    residents = {Englishman: "Englishman", Spaniard: "Spaniard", Ukrainian: "Ukrainian", Norwegian: "Norwegian", Japanese: "Japanese"}
    return residents[water]

def owns_zebra():
    (_, Englishman, Spaniard, Ukrainian, Norwegian, Japanese, _, _, _, _, _, _, _, _, _, zebra, _, _, _, _, _, _, _, _, _, _) = solve_zebra_puzzle()
    residents = {Englishman: "Englishman", Spaniard: "Spaniard", Ukrainian: "Ukrainian", Norwegian: "Norwegian", Japanese: "Japanese"}
    return residents[zebra]