def resistor_label(colors):
    significant_figures_codes = {
        "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
        "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9
    }
    multiplier_codes = {
        "black": 1, "brown": 10, "red": 100, "orange": 1_000, "yellow": 10_000,
        "green": 100_000, "blue": 1_000_000, "violet": 10_000_000, "grey": 100_000_000, "white": 1_000_000_000
    }
    tolerance_codes = {
        "brown": 1, "red": 2, "green": 0.5, "blue": 0.25, "violet": 0.1, "grey": 0.05, "gold": 5, "silver": 10
    }

    significant_figures = sum([
        significant_figures_codes[colors[i]] * (10 ** (len(colors) - i - 1))
        for i in range(len(colors) - 1)
    ])
    multiplier = multiplier_codes[colors[-1]]
    tolerance = tolerance_codes[colors[-2]] if len(colors) > 2 else 20

    resistor_value = significant_figures * multiplier
    unit = ""
    if resistor_value >= 1_000_000:
        resistor_value /= 1_000_000
        unit = "mega"
    elif resistor_value >= 1_000:
        resistor_value /= 1_000
        unit = "kilo"

    return f"{resistor_value} {unit}ohms ±{tolerance}%"