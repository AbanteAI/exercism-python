def label(colors):
    color_codes = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9,
    }

    resistance_value = (color_codes[colors[0]] * 10 + color_codes[colors[1]]) * 10 ** color_codes[colors[2]]

    if resistance_value >= 10 ** 9:
        value = resistance_value / 10 ** 9
        unit = "gigaohms"
    elif resistance_value >= 10 ** 6:
        value = resistance_value / 10 ** 6
        unit = "megaohms"
    elif resistance_value >= 10 ** 3:
        value = resistance_value / 10 ** 3
        unit = "kiloohms"
    else:
        value = resistance_value
        unit = "ohms"

    return f"{value} {unit}"