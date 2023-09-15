def largest_product(series, size):
    if size < 0:
        raise ValueError("span must not be negative")
    elif size > len(series):
        raise ValueError("span must be smaller than string length")
    if not series.isdigit():
        raise ValueError("digits input must only contain digits")

    largest = 0
    for i in range(len(series) - size + 1):
        span = series[i:i + size]
        product = 1
        for digit in span:
            product *= int(digit)
        if product > largest:
            largest = product

    return largest