def primes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for index, is_prime in enumerate(sieve):
        if is_prime:
            for multiple in range(index * index, limit + 1, index):
                sieve[multiple] = False

    return [number for number, prime in enumerate(sieve) if prime]