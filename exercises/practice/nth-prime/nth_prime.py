def prime(number):
    if number < 1:
        raise ValueError("Input number must be greater than or equal to 1")
    # Implement the logic to determine the nth prime number
    primes = [2]
    current_number = 3
    while len(primes) < number:
        is_prime = True
        for prime_number in primes:
            if current_number % prime_number == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(current_number)
        current_number += 2
    return primes[number - 1]
