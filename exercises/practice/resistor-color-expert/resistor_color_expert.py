def resistor_label(colors):
    color_code = {
        'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4,
        'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9
    }
    tolerance_code = {
        'grey': '0.05', 'violet': '0.1', 'blue': '0.25',
        'green': '0.5', 'brown': '1', 'red': '2',
        'gold': '5', 'silver': '10'
    }

    if len(colors) == 1 and colors[0] == 'black':
        return "0 ohms"

    value = ''.join(str(color_code[color]) for color in colors[:-2])
    multiplier = 10 ** color_code[colors[-2]]
    tolerance = tolerance_code[colors[-1]]
    resistance = int(value) * multiplier

    if resistance >= 1_000_000:
        resistance_value = resistance / 1_000_000
        resistance_str = f"{resistance_value:.0f}" if resistance_value.is_integer() else f"{resistance_value}"
        resistance_str += " megaohms"
    elif resistance >= 1_000:
        resistance_value = resistance / 1_000
        resistance_str = f"{resistance_value:.0f}" if resistance_value.is_integer() else f"{resistance_value}"
        resistance_str += " kiloohms"
    else:
        resistance_str = f"{resistance} ohms"

    return f"{resistance_str} ±{tolerance}%"