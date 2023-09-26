def get_solution():
    houses = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses))
    return next(
        (
            (red, green, ivory, yellow, blue),
            (Englishman, Spaniard, Ukrainian, Norwegian, Japanese),
            (dog, snails, fox, horse, zebra),
            (coffee, tea, milk, orange_juice, water),
            (Old_Gold, Kools, Chesterfields, Lucky_Strike, Parliaments),
        )
        for (red, green, ivory, yellow, blue) in orderings
        if red == 1  # The Englishman lives in the red house.
        for (Englishman, Spaniard, Ukrainian, Norwegian, Japanese) in orderings
        if Englishman == red  # The Englishman lives in the red house.
        if Norwegian == 1  # The Norwegian lives in the first house.
        if green == ivory + 1  # The green house is immediately to the right of the ivory house.
        for (dog, snails, fox, horse, zebra) in orderings
        if Spaniard == dog  # The Spaniard owns the dog.
        for (coffee, tea, milk, orange_juice, water) in orderings
        if coffee == green  # Coffee is drunk in the green house.
        if Ukrainian == tea  # The Ukrainian drinks tea.
        for (Old_Gold, Kools, Chesterfields, Lucky_Strike, Parliaments) in orderings
        if Old_Gold == snails  # The Old Gold smoker owns snails.
        if Kools == yellow  # Kools are smoked in the yellow house.
        if milk == 3  # Milk is drunk in the middle house.
        for (Englishman, Spaniard, Ukrainian, Norwegian, Japanese) in orderings
        if Norwegian == blue + 1 or Norwegian == blue - 1  # The Norwegian lives next to the blue house.
        for (Old_Gold, Kools, Chesterfields, Lucky_Strike, Parliaments) in orderings
        if Chesterfields == fox + 1 or Chesterfields == fox - 1  # The man who smokes Chesterfields lives in the house next to the man with the fox.
        for (Old_Gold, Kools, Chesterfields, Lucky_Strike, Parliaments) in orderings
        if Kools == horse + 1 or Kools == horse - 1  # Kools are smoked in the house next to the house where the horse is kept.
        if Lucky_Strike == orange_juice  # The Lucky Strike smoker drinks orange juice.
        if Japanese == Parliaments  # The Japanese smokes Parliaments.
    )

def drinks_water():
    water_drinker = None
    for house_color, house_nationality, house_pet, house_beverage, house_cigarette in get_solution():
        if house_beverage == 'water':
            water_drinker = house_nationality
            break
    return water_drinker
    water_drinker = None
    for house_color, house_nationality, house_pet, house_beverage, house_cigarette in get_solution():
        if house_beverage == 'water':
            water_drinker = house_nationality
            break
    return water_drinker
    pass


def owns_zebra():
    zebra_owner = None
    for house_color, house_nationality, house_pet, house_beverage, house_cigarette in get_solution():
        if house_pet == 'zebra':
            zebra_owner = house_nationality
            break
    return zebra_owner
    for house_color, house_nationality, house_pet, house_beverage, house_cigarette in get_solution():
        if house_pet == 'zebra':
            zebra_owner = house_nationality
            break
    return zebra_owner
