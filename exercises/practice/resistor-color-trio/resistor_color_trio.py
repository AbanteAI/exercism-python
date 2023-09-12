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
        "white": 9
    }

    resistor_value = (color_values[colors[0]] * 10 + color_values[colors[1]]) * (10 ** color_values[colors[2]])

    if resistor_value >= 10 ** 9:
        return f"{resistor_value // 10 ** 9} gigaohms"
    elif resistor_value >= 10 ** 6:
        return f"{resistor_value // 10 ** 6} megaohms"
    elif resistor_value >= 10 ** 3:
        return f"{resistor_value // 10 ** 3} kiloohms"
    else:
        return f"{resistor_value} ohms"