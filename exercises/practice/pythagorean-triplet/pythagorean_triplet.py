def triplets_with_sum(number):
    triplets = set()
    for m in range(2, int(number**0.5) + 1):
        for n in range(1, m):
            a = m**2 - n**2
            b = 2 * m * n
            c = m**2 + n**2
            k = 1
            while k * (a + b + c) <= number:
                if k * (a + b + c) == number:
                    triplets.add(tuple(sorted([k * a, k * b, k * c])))
                k += 1
    return [list(triplet) for triplet in triplets]