def maximum_value(maximum_weight, items):
    num_items = len(items)
    max_values = [[0] * (maximum_weight + 1) for _ in range(num_items + 1)]

    for i in range(1, num_items + 1):
        for w in range(1, maximum_weight + 1):
            item_weight = items[i - 1]["weight"]
            item_value = items[i - 1]["value"]

            if item_weight <= w:
                max_values[i][w] = max(
                    max_values[i - 1][w],
                    max_values[i - 1][w - item_weight] + item_value,
                )
            else:
                max_values[i][w] = max_values[i - 1][w]

    return max_values[num_items][maximum_weight]
