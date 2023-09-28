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
    first_color, second_color, third_color = colors
    main_value = color_values[first_color] * 10 + color_values[second_color]
    zeros = "0" * color_values[third_color]
    if main_value >= 1000:
        final_value = f"{main_value // 1000} kiloohms"
    else:
        final_value = f"{final_value} ohms"
    return final_value
