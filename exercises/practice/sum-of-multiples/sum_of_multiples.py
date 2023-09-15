def sum_of_multiples(limit, multiples):
    unique_multiples = set()
    for base_value in multiples:
        if base_value != 0:
            for multiple in range(base_value, limit, base_value):
        unique_multiples.add(multiple)
    return sum(unique_multiples)