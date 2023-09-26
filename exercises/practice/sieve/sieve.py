def primes(limit):
    if limit < 2:
        return []
    
    numbers = [True] * (limit + 1)
    numbers[0] = numbers[1] = False

    p = 2
    while p * p <= limit:
        if numbers[p]:
            for i in range(p * p, limit + 1, p):
                numbers[i] = False
        p += 1

    return [i for i, is_prime in enumerate(numbers) if is_prime]