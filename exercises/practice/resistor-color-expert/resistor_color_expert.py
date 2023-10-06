def resistor_label(colors):
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

    if len(colors) == 1:
        resistance = color_values[colors[0]]
        label = f"{resistance} ohms"
    elif len(colors) == 4:
        resistance = int(f"{color_values[colors[0]]}{color_values[colors[1]]}") * 10 ** color_values[colors[2]]
        tolerance = {
            "grey": 0.05,
            "violet": 0.1,
            "blue": 0.25,
            "green": 0.5,
            "brown": 1,
            "red": 2,
            "gold": 5,
            "silver": 10,
        }[colors[3]]
        label = f"{resistance} ohms ±{tolerance}%"
    elif len(colors) == 5:
        resistance = int(f"{color_values[colors[0]]}{color_values[colors[1]]}{color_values[colors[2]]}") * 10 ** color_values[colors[3]]
        tolerance = {
            "grey": 0.05,
            "violet": 0.1,
            "blue": 0.25,
            "green": 0.5,
            "brown": 1,
            "red": 2,
            "gold": 5,
            "silver": 10,
        }[colors[4]]
        label = f"{resistance} ohms ±{tolerance}%"
    else:
        label = "Invalid input"

    return label
