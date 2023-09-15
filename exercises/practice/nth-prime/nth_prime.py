def prime(number):
    if number < 1:
        raise ValueError("there is no zeroth prime")
    count = 0
    n = 2
    while count < number:
        if is_prime(n):
            count += 1
        n += 1
    return n - 1
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
