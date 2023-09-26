def sum_of_multiples(limit, multiples):
    unique_multiples = set()
        for num in range(base_value, limit, base_value) if base_value != 0 else [0]:
            if num != 0:
                unique_multiples.add(num)
    return sum(unique_multiples) if unique_multiples else 0
