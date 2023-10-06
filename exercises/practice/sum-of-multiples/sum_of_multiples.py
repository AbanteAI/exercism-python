def sum_of_multiples(limit, multiples):
    result = set()
    for num in multiples:
        if num == 0:
            continue
        for i in range(num, limit, num):
            result.add(i)
    return sum(result)
