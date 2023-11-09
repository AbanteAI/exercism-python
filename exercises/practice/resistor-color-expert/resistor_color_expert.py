def resistor_label(colors):
    color_values = {
        "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
        "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9
    }
    tolerance_values = {
        "grey": 0.05, "violet": 0.1, "blue": 0.25,
        "green": 0.5, "brown": 1, "red": 2, "gold": 5, "silver": 10
    }

    if len(colors) == 1 and colors[0] == "black":
        return "0 ohms"

    resistance = 0
    tolerance = ""
    if len(colors) == 4 or len(colors) == 5:
        if len(colors) == 4:
            resistance = (color_values[colors[0]] * 10 + color_values[colors[1]]) * (10 ** color_values[colors[2]])
            tolerance = tolerance_values[colors[3]]
        else:
            resistance = (color_values[colors[0]] * 100 + color_values[colors[1]] * 10 + color_values[colors[2]]) * (10 ** color_values[colors[3]])
            tolerance = tolerance_values[colors[4]]

        if resistance >= 1e6:
            resistance_str = f"{resistance / 1e6:.1f}" if resistance % 1e6 else f"{int(resistance // 1e6)}"
            resistance_str += " megaohms"
        elif resistance >= 1e3:
            resistance_str = f"{resistance / 1e3:.1f}" if resistance % 1e3 else f"{int(resistance // 1e3)}"
            resistance_str += " kiloohms"
        else:
            resistance_str = f"{resistance:.1f}" if resistance % 1 else f"{int(resistance)}"
            resistance_str += " ohms"

        return f"{resistance_str} ±{tolerance}%"
    else:
        raise ValueError("Invalid number of colors")
    pass
