def resistor_label(colors):
    color_values = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4,
                    'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}
    color_multipliers = {'black': 1, 'brown': 10, 'red': 100, 'orange': 1000, 'yellow': 10000,
                         'green': 100000, 'blue': 1000000, 'violet': 10000000, 'grey': 100000000, 'white': 1000000000}
    color_tolerances = {'grey': 0.05, 'violet': 0.1, 'blue': 0.25, 'green': 0.5, 'brown': 1, 'red': 2, 'gold': 5, 'silver': 10}

    num_bands = len(colors)
    if num_bands == 1 and colors[0] == "black":
        value = 0
        tolerance = ""
    elif num_bands == 4:
        value = (color_values[colors[0]] * 10 + color_values[colors[1]]) * color_multipliers[colors[2]]
        tolerance = color_tolerances[colors[3]]
    elif num_bands == 5:
        value = (color_values[colors[0]] * 100 + color_values[colors[1]] * 10 + color_values[colors[2]]) * color_multipliers[colors[3]]
        tolerance = color_tolerances[colors[4]]

    if value >= 1000000:
        value /= 1000000
        unit = "megaohms"
    elif value >= 1000:
        value /= 1000
        unit = "kiloohms"
    else:
        unit = "ohms"

    return f"{value:.0f} {unit} ±{tolerance}%" if float(value).is_integer() else f"{value} {unit} ±{tolerance}%"