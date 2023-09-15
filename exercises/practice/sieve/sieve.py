def primes(limit):
    if limit < 2:
        return []

    numbers = list(range(2, limit + 1))
    primes = []

    while numbers:
        prime = numbers.pop(0)
        primes.append(prime)

        numbers = [num for num in numbers if num % prime != 0]

    return primes