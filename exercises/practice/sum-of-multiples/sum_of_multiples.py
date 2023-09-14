def sum_of_multiples(limit, multiples):
    result = 0
    for i in range(limit):
        for multiple in multiples:
            if multiple != 0 and i % multiple == 0:
                result += i
                break
    return result