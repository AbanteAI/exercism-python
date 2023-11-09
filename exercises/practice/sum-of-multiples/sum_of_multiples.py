def sum_of_multiples(limit, multiples):
    unique_multiples = set()
    for multiple in multiples:
        if multiple == 0:
            continue
        unique_multiples.update(range(multiple, limit, multiple))
    return sum(unique_multiples)
