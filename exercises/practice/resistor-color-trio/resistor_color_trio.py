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
    value = (color_values[colors[0]] * 10 + color_values[colors[1]]) * 10 ** color_values[colors[2]]
    
    if value >= 1000000000:
        value /= 1000000000
        prefix = "gigaohms"
    elif value >= 1000000:
        value /= 1000000
        prefix = "megaohms"
    elif value >= 1000:
        value /= 1000
        prefix = "kiloohms"
    else:
        prefix = "ohms"
    
    return f"{int(value)} {prefix}"
