def prime(number):
    if number < 1:
        raise ValueError('there is no zeroth prime')
    
    def is_prime(num):
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

    count = 0
    prime_num = 1
    while count < number:
        prime_num += 1
        if is_prime(prime_num):
            count += 1
    return prime_num
