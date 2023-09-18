def label(colors):
    color_values = {
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

    main_value = color_values[colors[0]] * 10 + color_values[colors[1]]
    zeros = color_values[colors[2]]

    resistance_value = main_value * (10 ** zeros)

    if resistance_value >= 1000000:
        resistance_value /= 1000000
        unit = "megaohms"
    elif resistance_value >= 1000:
        resistance_value /= 1000
        unit = "kiloohms"
    else:
        unit = "ohms"

    return f"{resistance_value:.0f} {unit}"