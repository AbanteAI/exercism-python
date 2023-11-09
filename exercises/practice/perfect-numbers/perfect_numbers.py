def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    factors = set()
    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            factors.add(i)
            if i != number // i and i != 1:
                factors.add(number // i)
    aliquot_sum = sum(factors)

    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    else:
        return "deficient"
