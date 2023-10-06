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
    main_value = int("".join(str(color_values[color]) for color in colors[:2]))
    zeros = "0" * color_values[colors[2]]
    magnitude = ""
    if main_value >= 1000:
        magnitude = " kilo"
        main_value //= 1000
    return f"{main_value}{zeros}{magnitude} ohms"
