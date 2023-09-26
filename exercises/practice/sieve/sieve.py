def primes(limit):
    numbers = [True] * (limit + 1)
    numbers[0] = numbers[1] = False

    for i in range(2, int(limit ** 0.5) + 1):
        if numbers[i]:
            for j in range(i * i, limit + 1, i):
                numbers[j] = False

    return [i for i, is_prime in enumerate(numbers) if is_prime]