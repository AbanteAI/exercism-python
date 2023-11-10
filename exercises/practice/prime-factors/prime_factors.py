def factors(value):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    prime_factors = []
    divisor = 2
    while value > 1:
        while value % divisor == 0:
            prime_factors.append(divisor)
            value //= divisor
        divisor += 1
        while not is_prime(divisor) and divisor <= value:
            divisor += 1
    return prime_factors