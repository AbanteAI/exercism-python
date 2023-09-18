def largest_product(series, size):
    if size < 0:
        raise ValueError("span must not be negative")
    if size > len(series):
        raise ValueError("span must be smaller than string length")
    if not series:
        return 1
        raise ValueError("digits input must only contain digits")
        return 1
    largest_product = 0
    for i in range(len(series) - size + 1):
        current_series = series[i:i + size]
        product = 1
        for digit in current_series:
            product *= int(digit)
        largest_product = max(largest_product, product)
    return largest_product