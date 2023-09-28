def resistor_label(colors):
    color_values = {
        "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
        "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9
    }
    tolerance_values = {
        "grey": 0.05, "violet": 0.1, "blue": 0.25, "green": 0.5,
        "brown": 1, "red": 2, "gold": 5, "silver": 10
    }

    if len(colors) == 1:
        return "0 ohms"

    main_value = 0
    multiplier = 1
    tolerance = 0

    if len(colors) == 4:
        main_value = color_values[colors[0]] * 10 + color_values[colors[1]]
        multiplier = 10 ** color_values[colors[2]]
        tolerance = tolerance_values[colors[3]]
    elif len(colors) == 5:
        main_value = color_values[colors[0]] * 100 + color_values[colors[1]] * 10 + color_values[colors[2]]
        multiplier = 10 ** color_values[colors[3]]
        tolerance = tolerance_values[colors[4]]

    ohms = main_value * multiplier

    if ohms >= 1000000:
        ohms /= 1000000
        unit = "megaohms"
    elif ohms >= 1000:
        ohms /= 1000
        unit = "kiloohms"
    else:
        unit = "ohms"

    return f"{ohms:.2f} {unit} ±{tolerance}%" if ohms != round(ohms) and ohms * 10 != round(ohms * 10) else f"{ohms:.1f} {unit} ±{tolerance}%" if ohms != round(ohms) else f"{ohms:.0f} {unit} ±{tolerance}%"