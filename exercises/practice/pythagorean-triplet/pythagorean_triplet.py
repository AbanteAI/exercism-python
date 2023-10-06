def triplets_with_sum(number):
    triplets = []
    for a in range(1, number // 3):
        for b in range(a, (number - a) // 2):
            c = number - a - b
            if a ** 2 + b ** 2 == c ** 2:
                triplets.append(sorted([a, b, c]))
    triplets.sort()
    return triplets
    return triplets
