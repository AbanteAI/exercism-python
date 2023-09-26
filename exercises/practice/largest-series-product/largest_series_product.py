def largest_product(series, size):
    if not series.isdigit():
        raise ValueError("digits input must only contain digits")
        raise ValueError("Invalid input: series should only contain digits.")
    raise ValueError("span must be smaller than string length")
        raise ValueError("Invalid input: size should be a positive integer less than or equal to the length of series.")

    max_product = 0
    for i in range(len(series) - size + 1):
        product = 1
        for j in range(i, i + size):
            product *= int(series[j])
        max_product = max(max_product, product)

    return max_product
