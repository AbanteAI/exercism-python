def solve_puzzle():
    # Houses: 1, 2, 3, 4, 5
    # Order: [color, nationality, pet, drink, smoke]
    # All possible permutations of properties
    import itertools
    colors = ['red', 'green', 'ivory', 'yellow', 'blue']
    nationalities = ['Englishman', 'Spaniard', 'Ukrainian', 'Norwegian', 'Japanese']
    pets = ['dog', 'snails', 'fox', 'horse', 'zebra']
    drinks = ['coffee', 'tea', 'milk', 'orange juice', 'water']
    smokes = ['Old Gold', 'Kools', 'Chesterfields', 'Lucky Strike', 'Parliaments']

    # Generate all possible permutations of houses
    permutations = list(itertools.permutations(range(5)))
    for colors_perm in permutations:
        if colors_perm.index(0) != colors_perm.index(1) - 1:  # Rule 6
            continue
        for nationalities_perm in permutations:
            if nationalities_perm[0] != 3 or nationalities_perm[colors_perm.index(0)] != 0:  # Rule 10 and 15
                continue
            for pets_perm in permutations:
                if nationalities_perm.index(1) != pets_perm.index(0):  # Rule 3
                    continue
                for drinks_perm in permutations:
                    if drinks_perm[2] != 2 or colors_perm.index(2) != drinks_perm.index(0):  # Rule 9 and 4
                        continue
                    if nationalities_perm.index(2) != drinks_perm.index(1):  # Rule 5
                        continue
                    for smokes_perm in permutations:
                        if smokes_perm.index(0) != pets_perm.index(1) or smokes_perm.index(1) != colors_perm.index(3):  # Rule 7 and 8
                            continue
                        if abs(smokes_perm.index(2) - pets_perm.index(2)) != 1 or abs(smokes_perm.index(1) - pets_perm.index(3)) != 1:  # Rule 11 and 12
                            continue
                        if smokes_perm.index(3) != drinks_perm.index(3) or nationalities_perm.index(4) != smokes_perm.index(4):  # Rule 13 and 14
                            continue

                        # If all conditions are met, return the solution
                        houses = [None] * 5
                        for i in range(5):
                            houses[i] = (
                                colors[colors_perm[i]],
                                nationalities[nationalities_perm[i]],
                                pets[pets_perm[i]],
                                drinks[drinks_perm[i]],
                                smokes[smokes_perm[i]]
                            )
                        return houses
    return None  # If no solution is found

def drinks_water():
    solution = solve_puzzle()
    if solution:
        water_drinker = next(h for h in solution if h[3] == 'water')
        return water_drinker[1]
    return "No solution found"

def owns_zebra():
    solution = solve_puzzle()
    if solution:
        zebra_owner = next(h for h in solution if h[2] == 'zebra')
        return zebra_owner[1]
    return "No solution found"
