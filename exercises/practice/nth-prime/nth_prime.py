def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime(number):
    if number < 1:
        raise ValueError("there is no zeroth prime")
    count = 0
    candidate = 2
    while count < number:
        if is_prime(candidate):
            count += 1
        if count == number:
            return candidate
        candidate += 1