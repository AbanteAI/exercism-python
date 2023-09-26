def prime(number):
    if number < 1:
    raise ValueError("there is no zeroth prime")

    primes = []
    current_number = 2

    while len(primes) < number:
        is_prime = True

        for prime in primes:
            if current_number % prime == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(current_number)

        current_number += 1

    return primes[-1]
