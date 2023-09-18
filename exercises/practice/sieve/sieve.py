def primes(limit):
    if limit < 2:
        return []

    numbers = list(range(2, limit + 1))
    is_prime = [True] * len(numbers)

    for i, number in enumerate(numbers):
        if is_prime[i]:
            for multiple in range(number * 2, limit + 1, number):
                is_prime[numbers.index(multiple)] = False

    return [number for i, number in enumerate(numbers) if is_prime[i]]
