def primes(limit):
    # Create a list of numbers from 2 to the given limit
    numbers = list(range(2, limit + 1))

    # Use Sieve of Eratosthenes algorithm to find prime numbers
    primes = []
    while numbers:
        prime = numbers[0]
        primes.append(prime)
        numbers = [n for n in numbers if n % prime != 0]

    return primes
