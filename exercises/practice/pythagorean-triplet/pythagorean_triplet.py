def triplets_with_sum(number):
    triplets = []
    for a in range(1, number // 3):
        b = (number**2 - 2*number*a) / (2*number - 2*a)
        if b.is_integer():
            b = int(b)
            c = number - a - b
            if a < b < c:
                triplets.append([a, b, c])
    return triplets