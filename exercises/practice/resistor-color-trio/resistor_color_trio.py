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
        "white": 9
    }

    value = (color_codes[colors[0]] * 10 + color_codes[colors[1]]) * (10 ** color_codes[colors[2]])

    if value >= 1000000:
        value /= 1000000
        unit = "megaohms"
    elif value >= 1000:
        value /= 1000
        unit = "kiloohms"
    else:
        unit = "ohms"

    return f"{value:.0f} {unit}"