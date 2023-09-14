def resistor_label(colors):
    color_values = {
        "black": (0, None),
        "brown": (1, 1),
        "red": (2, 2),
        "orange": (3, None),
        "yellow": (4, 5),
        "green": (5, 0.5),
        "blue": (6, 0.25),
        "violet": (7, 0.1),
        "grey": (8, 0.05),
        "white": (9, None)
    }

    resistance = 0
    for i, color in enumerate(colors[:-1]):
        value, _ = color_values[color]
        resistance += value * (10 ** (len(colors) - i - 3))

    _, tolerance = color_values[colors[-1]]

    if resistance >= 1e6:
        resistance /= 1e6
        unit = "megaohms"
    elif resistance >= 1e3:
        resistance /= 1e3
        unit = "kiloohms"
    else:
        unit = "ohms"

    return f"{resistance} {unit} ±{tolerance}%" if tolerance else f"{resistance} {unit}"