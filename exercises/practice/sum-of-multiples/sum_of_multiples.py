def sum_of_multiples(limit, multiples):
    unique_multiples = set()
    for multiple in multiples:
        for i in range(multiple, limit, multiple):
            unique_multiples.add(i)
    return sum(unique_multiples)