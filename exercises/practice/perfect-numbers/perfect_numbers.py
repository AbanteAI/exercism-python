def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
def get_factors(number):
    factors = set()
    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            factors.add(i)
            factors.add(number // i)
    return factors

def classify(number):
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    
    factors = get_factors(number)
    factors.remove(number)
    factor_sum = sum(factors)

    if factor_sum == number:
        return "perfect"
    elif factor_sum > number:
        return "abundant"
    else:
        return "deficient"
