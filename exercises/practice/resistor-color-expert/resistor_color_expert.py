COLOR_VALUES = {
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

TOLERANCE_VALUES = {
    "grey": 0.05,
    "violet": 0.1,
    "blue": 0.25,
    "green": 0.5,
    "brown": 1,
    "red": 2,
    "gold": 5,
    "silver": 10
}
def resistor_label(colors):
    if len(colors) == 1:
        return f"{COLOR_VALUES[colors[0]]} ohms"
    elif len(colors) == 4:
        main_value = int(f"{COLOR_VALUES[colors[0]]}{COLOR_VALUES[colors[1]]}") * (10 ** COLOR_VALUES[colors[2]])
        tolerance = TOLERANCE_VALUES[colors[3]]
        return f"{main_value} ohms ±{tolerance}%"
    elif len(colors) == 5:
        main_value = int(f"{COLOR_VALUES[colors[0]]}{COLOR_VALUES[colors[1]]}{COLOR_VALUES[colors[2]]}") * (10 ** COLOR_VALUES[colors[3]])
        tolerance = TOLERANCE_VALUES[colors[4]]
        if main_value >= 1000000:
            return f"{main_value // 1000000} megaohms ±{tolerance}%"
        elif main_value >= 1000:
            return f"{main_value // 1000} kiloohms ±{tolerance}%"
        else:
            return f"{main_value} ohms ±{tolerance}%"
