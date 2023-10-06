def primes(limit):
    numbers = [True] * (limit + 1)
    numbers[0], numbers[1] = False, False
    for number in range(2, int(limit**0.5) + 1):
        if numbers[number]:
            for multiple in range(number * number, limit + 1, number):
                numbers[multiple] = False
    return [number for number in range(2, limit + 1) if numbers[number]]