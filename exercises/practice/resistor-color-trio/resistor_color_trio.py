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
    value = (color_values[colors[0]] * 10 + color_values[colors[1]]) * (10 ** color_values[colors[2]])
    zeros = ""
    magnitude = ""
    if value >= 1000:
        value /= 1000
        magnitude = " kilo"
    return f"{int(value)}{zeros} ohms{magnitude}"
