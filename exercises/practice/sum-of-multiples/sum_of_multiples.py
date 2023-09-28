def sum_of_multiples(level, base_values):
    multiples = set()
    for base_value in base_values:
        for i in range(base_value, level, base_value):
            multiples.add(i)
    return sum(multiples)
