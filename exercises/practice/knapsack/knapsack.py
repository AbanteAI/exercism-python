def maximum_value(maximum_weight, items):
def maximum_value(maximum_weight, items):
    total_value = 0
    for item in items:
        if item["weight"] <= maximum_weight:
            total_value += item["value"]
            maximum_weight -= item["weight"]
    return total_value
