def resistor_label(colors):
    color_values = {
        'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4,
        'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9
    }
    tolerance_values = {
        'grey': '0.05', 'violet': '0.1', 'blue': '0.25', 'green': '0.5',
        'brown': '1', 'red': '2', 'gold': '5', 'silver': '10'
    }

    if len(colors) == 1 and colors[0] == 'black':
        return "0 ohms"

    if len(colors) in [4, 5]:
        value = ''.join(str(color_values[color]) for color in colors[:-2])
        multiplier = 10 ** color_values[colors[-2]]
        tolerance = tolerance_values[colors[-1]]
        resistance = int(value) * multiplier

        if resistance >= 1_000_000:
            resistance_str = "{:.0f} megaohms".format(resistance / 1_000_000)
        elif resistance >= 1_000:
            resistance_str = "{:.0f} kiloohms".format(resistance / 1_000)
        else:
            resistance_str = "{:.0f} ohms".format(resistance)

        return f"{resistance_str} ±{tolerance}%"
    else:
        raise ValueError("Invalid number of colors")