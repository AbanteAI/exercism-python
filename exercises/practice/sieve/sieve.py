def primes(limit):
    # Create a list of all numbers from 2 to the given limit
    numbers = list(range(2, limit + 1))

    # Iterate through the list and mark all multiples of each prime number as composite
    for i in range(2, int(limit ** 0.5) + 1):
        if numbers[i - 2] != 0:
            for j in range(i * i, limit + 1, i):
                numbers[j - 2] = 0

    # Return the list of unmarked numbers as the list of prime numbers
    return [num for num in numbers if num != 0]
