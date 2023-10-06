def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
def classify(number):
    if not isinstance(number, int) or number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    
    factors_sum = 1
    sqrt_num = int(number ** 0.5)
    for i in range(2, sqrt_num + 1):
        if number % i == 0:
            factors_sum += i
            if i != number // i:
                factors_sum += number // i
        return "perfect"
    elif factors_sum > number:
        return "abundant"
    else:
        return "deficient"
