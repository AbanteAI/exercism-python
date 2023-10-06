def resistor_label(colors):
    color_values = {
        "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
        "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9
    }

    tolerance_values = {
        "grey": 0.05, "violet": 0.1, "blue": 0.25, "green": 0.5,
        "brown": 1, "red": 2, "gold": 5, "silver": 10
    }

    num_colors = len(colors)
    if num_colors == 1:
        value = 0
        tolerance = ""
    elif num_colors == 4:
        value = (color_values[colors[0]] * 10 + color_values[colors[1]]) * (10 ** color_values[colors[2]])
        tolerance = f"±{tolerance_values[colors[3]]}%"
    elif num_colors == 5:
        value = (color_values[colors[0]] * 100 + color_values[colors[1]] * 10 + color_values[colors[2]]) * (10 ** color_values[colors[3]])
        tolerance = f"±{tolerance_values[colors[4]]}%"
    else:
        raise ValueError("Invalid number of colors")

    if value >= 1000000:
        value /= 1000000
        unit = "megaohms"
    elif value >= 1000:
        value /= 1000
        unit = "kiloohms"
    else:
        unit = "ohms"

    return f"{value:.0f if value.is_integer() else value} {unit} {tolerance}".strip()