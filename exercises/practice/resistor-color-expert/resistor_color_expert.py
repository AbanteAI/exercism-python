def resistor_label(colors):
    value_code = {
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
    multiplier_code = {
        "black": 1,
        "brown": 10,
        "red": 100,
        "orange": 1000,
        "yellow": 10000,
        "green": 100000,
        "blue": 1000000,
        "violet": 10000000,
        "grey": 100000000,
        "white": 1000000000
    }
    tolerance_code = {
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
        value = 0
        tolerance = 0
    elif len(colors) == 4:
        value = (value_code[colors[0]] * 10 + value_code[colors[1]]) * multiplier_code[colors[2]]
        tolerance = tolerance_code[colors[3]]
    elif len(colors) == 5:
        value = (value_code[colors[0]] * 100 + value_code[colors[1]] * 10 + value_code[colors[2]]) * multiplier_code[colors[3]]
        tolerance = tolerance_code[colors[4]]

    if value >= 1000000:
        value = value / 1000000
        unit = "megaohms"
    elif value >= 1000:
        value = value / 1000
        unit = "kiloohms"
    else:
        unit = "ohms"

    return f"{value:.0f if value.is_integer() else value} {unit} ±{tolerance:.2f if tolerance < 1 else int(tolerance)}%"