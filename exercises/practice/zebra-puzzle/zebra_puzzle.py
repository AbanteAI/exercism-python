def drinks_water():
    pass


def owns_zebra():
    pass

from itertools import permutations

def generate_permutations():
    colors = ["Red", "Green", "Ivory", "Yellow", "Blue"]
    nationalities = ["Englishman", "Spaniard", "Ukrainian", "Norwegian", "Japanese"]
    pets = ["Dog", "Snails", "Fox", "Horse", "Zebra"]
    drinks = ["Coffee", "Tea", "Milk", "Orange Juice", "Water"]
    cigarettes = ["Old Gold", "Kools", "Chesterfields", "Lucky Strike", "Parliaments"]

    for color_permutation in permutations(colors):
        if "Ivory" in color_permutation and "Green" in color_permutation and color_permutation.index("Ivory") + 1 == color_permutation.index("Green"):
            for nationality_permutation in permutations(nationalities):
                if nationality_permutation.index("Norwegian") == 0 and "Blue" in nationality_permutation and nationality_permutation.index("Blue") == 1:
                    for pet_permutation in permutations(pets):
                        for drink_permutation in permutations(drinks):
                            if drink_permutation.index("Milk") == 2:
                                for cigarette_permutation in permutations(cigarettes):
                                    yield (color_permutation, nationality_permutation, pet_permutation, drink_permutation, cigarette_permutation)

def is_valid_permutation(p):
    colors, nationalities, pets, drinks, cigarettes = p

    for i in range(5):
        if (nationalities[i] == "Englishman" and colors[i] != "Red") or (colors[i] == "Red" and nationalities[i] != "Englishman"):
            return False
        if (nationalities[i] == "Spaniard" and pets[i] != "Dog") or (pets[i] == "Dog" and nationalities[i] != "Spaniard"):
            return False
        if (colors[i] == "Green" and drinks[i] != "Coffee") or (drinks[i] == "Coffee" and colors[i] != "Green"):
            return False
        if (nationalities[i] == "Ukrainian" and drinks[i] != "Tea") or (drinks[i] == "Tea" and nationalities[i] != "Ukrainian"):
            return False
        if (cigarettes[i] == "Old Gold" and pets[i] != "Snails") or (pets[i] == "Snails" and cigarettes[i] != "Old Gold"):
            return False
        if (cigarettes[i] == "Kools" and colors[i] != "Yellow") or (colors[i] == "Yellow" and cigarettes[i] != "Kools"):
            return False
        if (cigarettes[i] == "Chesterfields" and (pets[i - 1] != "Fox" and pets[i + 1] != "Fox")):
            return False
        if (cigarettes[i] == "Kools" and (pets[i - 1] != "Horse" and pets[i + 1] != "Horse")):
            return False
        if (cigarettes[i] == "Lucky Strike" and drinks[i] != "Orange Juice") or (drinks[i] == "Orange Juice" and cigarettes[i] != "Lucky Strike"):
            return False
        if (nationalities[i] == "Japanese" and cigarettes[i] != "Parliaments") or (cigarettes[i] == "Parliaments" and nationalities[i] != "Japanese"):
            return False

    return True

    return True

def drinks_water():
    for p in generate_permutations():
        if is_valid_permutation(p):
            _, nationalities, _, drinks, _ = p
            return nationalities[drinks.index("Water")]

def owns_zebra():
    for p in generate_permutations():
        if is_valid_permutation(p):
            _, nationalities, pets, _, _ = p
            return nationalities[pets.index("Zebra")]