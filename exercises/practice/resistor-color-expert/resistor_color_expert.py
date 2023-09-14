def resistor_label(colors):
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

    value = int("".join(str(color_codes[color]) for color in colors[:-1]))
    multiplier = 10 ** color_codes[colors[-2]]
    tolerance = {
        "brown": "±1%",
        "red": "±2%",
        "green": "±0.5%",
        "blue": "±0.25%",
        "violet": "±0.1%",
        "grey": "±0.05%",
        "gold": "±5%",
        "silver": "±10%",
    }[colors[-1]]

    if value >= 1_000_000:
        value /= 1_000_000
        unit = "megaohms"
    elif value >= 1_000:
        value /= 1_000
        unit = "kiloohms"
    else:
        unit = "ohms"

    return f"{value:.2f} {unit} {tolerance}"