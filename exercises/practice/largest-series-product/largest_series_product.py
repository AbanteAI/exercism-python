def largest_product(series, size):
    if size == 0:
        return 1

    largest = 0
    for i in range(len(series) - size + 1):
        product = 1
        for j in range(size):
            product *= int(series[i + j])
        largest = max(largest, product)

    return largest
