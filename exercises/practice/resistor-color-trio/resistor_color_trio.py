def label(colors):
    color_values = {
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
    first_color = color_values[colors[0]]
    second_color = color_values[colors[1]]
    third_color = color_values[colors[2]]

    resistance_value = (first_color * 10 + second_color) * 10 ** third_color

    metric_prefixes = ["", "kilo", "mega", "giga", "tera"]
    prefix_index = 0

    while resistance_value >= 1000 and prefix_index < len(metric_prefixes):
        resistance_value /= 1000
        prefix_index += 1

    metric_prefix = metric_prefixes[prefix_index]
    return f"{int(resistance_value)} {metric_prefix} ohms"
    return f"{resistance_value} {metric_prefix}ohms"