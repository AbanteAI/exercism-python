def primes(limit):
    if limit < 2:
        return []

    numbers = list(range(2, limit + 1))
    for i in numbers:
        if i is not None:
            for multiple in range(i * 2, limit + 1, i):
                numbers[multiple - 2] = None

    return [num for num in numbers if num is not None]