def prime(number):
    if number < 1:
        raise ValueError("there is no zeroth prime")
    
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
    
    count = 0
    num = 1
    while count < number:
        num += 1
        if is_prime(num):
            count += 1
    return num
