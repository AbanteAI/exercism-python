def resistor_label(colors):
    values = {
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
    tolerances = {
        "grey": 0.05,
        "violet": 0.1,
        "blue": 0.25,
        "green": 0.5,
        "brown": 1,
        "red": 2,
        "gold": 5,
        "silver": 10
    }

    if len(colors) == 1:
        resistance = values[colors[0]]
        label = f"{resistance} ohms"
    elif len(colors) == 4:
        resistance = (values[colors[0]] * 10 + values[colors[1]]) * (10 ** values[colors[2]])
        tolerance = tolerances[colors[3]]
        label = f"{resistance} ohms ±{tolerance}%"
    elif len(colors) == 5:
        resistance = (values[colors[0]] * 100 + values[colors[1]] * 10 + values[colors[2]]) * (10 ** values[colors[3]])
        tolerance = tolerances[colors[4]]
        label = f"{resistance} ohms ±{tolerance}%"

    if resistance >= 1000000:
        resistance /= 1000000
        unit = "megaohms"
    elif resistance >= 1000:
        resistance /= 1000
        unit = "kiloohms"
    else:
        unit = "ohms"

    label = f"{int(resistance)} {unit} ±{tolerance}%"
    return label
