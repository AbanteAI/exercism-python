def prime(number):
    pass
def is_prime(num):
    """Check if a number is a prime number."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def prime(number):
    """Find the nth prime number."""
    if number < 1:
        raise ValueError('there is no zeroth prime')
    
    count = 0
    num = 2
    while True:
        if is_prime(num):
            count += 1
            if count == number:
                return num
        num += 1
