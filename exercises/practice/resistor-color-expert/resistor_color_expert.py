def resistor_label(colors):
    value = 0
    tolerance = 0

    if len(colors) == 1:
        if colors[0] == "black":
            return "0 ohms 0%"
    elif len(colors) == 4:
        value = colors_to_value(colors[:3])
        tolerance = colors_to_tolerance(colors[3])
    elif len(colors) == 5:
        value = colors_to_value(colors[:3]) * colors_to_multiplier(colors[3])
        tolerance = colors_to_tolerance(colors[4])

    if value >= 1000000:
        return f"{value // 1000000} megaohms ±{tolerance}%"
    elif value >= 1000:
        return f"{value // 1000} kiloohms ±{tolerance}%"
    else:
        return f"{value} ohms ±{tolerance}%"

    if len(colors) == 1:
        if colors[0] == "black":
            return "0 ohms 0%"
    elif len(colors) == 4:
        value = colors_to_value(colors[:3])
        tolerance = colors_to_tolerance(colors[3])
    elif len(colors) == 5:
        value = colors_to_value(colors[:3]) * colors_to_multiplier(colors[3])
        tolerance = colors_to_tolerance(colors[4])

    if value >= 1000000:
        return f"{value // 1000000} megaohms ±{tolerance}%"
    elif value >= 1000:
        return f"{value // 1000} kiloohms ±{tolerance}%"
    else:
        return f"{value} ohms ±{tolerance}%"