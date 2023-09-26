def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def prime(nth):
    if nth < 1:
raise ValueError("there is no zeroth prime")

    primes = []
    number = 2
    while len(primes) < nth:
        if is_prime(number):
            primes.append(number)
        number += 1

    return primes[-1]