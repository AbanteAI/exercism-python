def primes(limit):
    if limit < 2:
        return []

    sieve = [True] * (limit + 1)
    sieve[0] = False
    sieve[1] = False

    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit + 1, i):
                sieve[j] = False

    return [i for i in range(2, limit + 1) if sieve[i]]