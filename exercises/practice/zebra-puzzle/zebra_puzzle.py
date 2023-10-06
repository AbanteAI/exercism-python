from itertools import permutations

def drinks_water():
    houses = list(range(1, 6))
    orderings = list(permutations(houses))

    for (red, green, ivory, yellow, blue) in orderings:
        if not (ivory + 1 == green): continue
        for (Englishman, Spaniard, Ukrainian, Norwegian, Japanese) in orderings:
            if not (Englishman == red): continue
            if not (Norwegian == 1): continue
            if not (next_to(Norwegian, blue)): continue
            for (dog, snails, fox, horse, ZEBRA) in orderings:
                if not (Spaniard == dog): continue
                for (coffee, tea, milk, orange_juice, WATER) in orderings:
                    if not (coffee == green): continue
                    if not (Ukrainian == tea): continue
                    if not (milk == 3): continue
                    for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings:
                        if not (Kools == yellow): continue
                        if not (OldGold == snails): continue
                        if not (next_to(Chesterfields, fox)): continue
                        if not (next_to(Kools, horse)): continue
                        if not (LuckyStrike == orange_juice): continue
                        if not (Japanese == Parliaments): continue

                        return {1: "Norwegian", 2: "Englishman", 3: "Ukrainian", 4: "Spaniard", 5: "Japanese"}[WATER]

def next_to(a, b):
    return abs(a - b) == 1


def owns_zebra():
    houses = list(range(1, 6))
    orderings = list(permutations(houses))

    for (red, green, ivory, yellow, blue) in orderings:
        if not (ivory + 1 == green): continue
        for (Englishman, Spaniard, Ukrainian, Norwegian, Japanese) in orderings:
            if not (Englishman == red): continue
            if not (Norwegian == 1): continue
            if not (next_to(Norwegian, blue)): continue
            for (dog, snails, fox, horse, ZEBRA) in orderings:
                if not (Spaniard == dog): continue
                for (coffee, tea, milk, orange_juice, WATER) in orderings:
                    if not (coffee == green): continue
                    if not (Ukrainian == tea): continue
                    if not (milk == 3): continue
                    for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings:
                        if not (Kools == yellow): continue
                        if not (OldGold == snails): continue
                        if not (next_to(Chesterfields, fox)): continue
                        if not (next_to(Kools, horse)): continue
                        if not (LuckyStrike == orange_juice): continue
                        if not (Japanese == Parliaments): continue

                        return {1: "Norwegian", 2: "Englishman", 3: "Ukrainian", 4: "Spaniard", 5: "Japanese"}[ZEBRA]

def next_to(a, b):
    return abs(a - b) == 1
