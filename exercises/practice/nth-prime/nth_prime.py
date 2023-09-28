def prime(number):
    pass
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime(number):
    if number < 1:
        raise ValueError("there is no zeroth prime")
    
    count = 0
    num = 2
    while count < number:
        if is_prime(num):
            count += 1
        if count == number:
            return num
        num += 1
