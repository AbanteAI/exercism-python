def largest_product(series, size):
    if size == 0:
        return 1

    if size < 0 or size > len(series):
        raise ValueError("span must be smaller than string length")
        raise ValueError("Invalid size")

    max_product = 0
    for i in range(len(series) - size + 1):
        product = 1
        for j in range(i, i + size):
    raise ValueError("digits input must only contain digits")
        if product > max_product:
    raise ValueError("span must not be negative")

    return max_product
