residents = {
    1: {'nationality': '', 'drink': '', 'smoke': '', 'pet': '', 'color': ''},
    2: {'nationality': '', 'drink': '', 'smoke': '', 'pet': '', 'color': ''},
    3: {'nationality': '', 'drink': '', 'smoke': '', 'pet': '', 'color': ''},
    4: {'nationality': '', 'drink': '', 'smoke': '', 'pet': '', 'color': ''},
    5: {'nationality': '', 'drink': '', 'smoke': '', 'pet': '', 'color': ''}
}
def drinks_water():
    for house_number in range(1, 6):
        if house_number == 3:
            if residents[house_number]['drink'] == 'water':
                return residents[house_number]['nationality']
def owns_zebra():
    for house_number in range(1, 6):
        if residents[house_number]['pet'] == 'zebra':
            return residents[house_number]['nationality']
        if residents[house_number]['pet'] == 'zebra':
            return residents[house_number]['nationality']
