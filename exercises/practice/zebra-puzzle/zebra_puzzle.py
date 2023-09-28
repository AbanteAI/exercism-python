residents = [
    {"nationality": "Englishman", "color": "", "drink": "", "smoke": "", "pet": ""},
    {"nationality": "Spaniard", "color": "", "drink": "", "smoke": "", "pet": ""},
    {"nationality": "Ukrainian", "color": "", "drink": "", "smoke": "", "pet": ""},
    {"nationality": "Norwegian", "color": "", "drink": "", "smoke": "", "pet": ""},
    {"nationality": "Japanese", "color": "", "drink": "", "smoke": "", "pet": ""}
]
def drinks_water():
    # Implement logic to determine which resident drinks water
    for house in range(1, 6):
        if house == 1:
            if "water" in residents[house]:
                return residents[house]["nationality"]
        elif house == 2:
            if residents[house - 1]["color"] == "green":
                if "water" in residents[house]:
                    return residents[house]["nationality"]
        elif house == 3:
            if residents[house - 1]["drink"] == "milk":
                if "water" in residents[house]:
                    return residents[house]["nationality"]
        elif house == 4:
            if residents[house - 1]["nationality"] == "Norwegian":
                if "water" in residents[house]:
                    return residents[house]["nationality"]
        elif house == 5:
            if "water" in residents[house]:
                return residents[house]["nationality"]

def owns_zebra():
    # Implement logic to determine who owns the zebra
    for house in range(1, 6):
        if "zebra" in residents[house]:
            return residents[house]["nationality"]