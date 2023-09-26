def sum_of_multiples(limit, multiples):
    unique_multiples = set()
    for base_value in multiples:
        if base_value == 0:
            continue
        for num in range(base_value, limit, base_value):
            unique_multiples.add(num)