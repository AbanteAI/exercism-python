COLOR_CODES = {
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

def label(colors):
    if not all(color in COLOR_CODES for color in colors):
        raise ValueError("Invalid color in the list")

    value = (COLOR_CODES[colors[0]] * 10 + COLOR_CODES[colors[1]]) * (10 ** COLOR_CODES[colors[2]])
    if value < 1000:
        return f"{value} ohms"
    elif value < 1_000_000:
        value //= 1000
        return f"{value} kiloohms"
    elif value < 1_000_000_000:
        value //= 1_000_000
        return f"{value} megaohms"
    else:
        value //= 1_000_000_000
        return f"{value} gigaohms"