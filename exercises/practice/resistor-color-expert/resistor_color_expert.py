def resistor_label(colors):
    color_values = {
        "black": 0,
        "brown": 1,
def resistor_label(colors):
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
        "white": 9,
    }

    tolerance_values = {
        "brown": 1,
        "red": 2,
        "green": 0.5,
        "blue": 0.25,
        "violet": 0.1,
        "grey": 0.05,
        "gold": 5,
        "silver": 10,
    }

    main_value = 0
    tolerance = ""

    if len(colors) == 4:
        main_value = int(str(color_values[colors[0]]) + str(color_values[colors[1]])) * 10 ** color_values[colors[2]]
        tolerance = tolerance_values[colors[3]]
    elif len(colors) == 5:
        main_value = int(str(color_values[colors[0]]) + str(color_values[colors[1]]) + str(color_values[colors[2]])) * 10 ** color_values[colors[3]]
        tolerance = tolerance_values[colors[4]]

    if main_value >= 1000000:
        main_value = str(main_value // 1000000) + " megaohms"
    elif main_value >= 1000:
        main_value = str(main_value // 1000) + " kiloohms"
    else:
        main_value = str(main_value) + " ohms"

    return main_value + " ±" + str(tolerance) + "%"
    }

    main_value = 0
    tolerance = ""

    if len(colors) == 4:
        main_value = int(str(color_values[colors[0]]) + str(color_values[colors[1]])) * 10 ** color_values[colors[2]]
        tolerance = color_values[colors[3]]
    elif len(colors) == 5:
        main_value = int(str(color_values[colors[0]]) + str(color_values[colors[1]]) + str(color_values[colors[2]])) * 10 ** color_values[colors[3]]
        tolerance = color_values[colors[4]]

    if main_value >= 1000000:
        main_value = str(main_value // 1000000) + " megaohms"
    elif main_value >= 1000:
        main_value = str(main_value // 1000) + " kiloohms"
    else:
        main_value = str(main_value) + " ohms"

    return main_value + " ±" + str(tolerance) + "%"