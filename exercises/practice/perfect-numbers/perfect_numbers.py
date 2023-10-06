def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    def aliquot_sum(num):
        factors = []
        for i in range(1, (num // 2) + 1):
            if num % i == 0:
                factors.append(i)
        return sum(factors)

    sum_of_factors = aliquot_sum(number)

    if sum_of_factors == number:
        return "perfect"
    elif sum_of_factors > number:
        return "abundant"
    else:
        return "deficient"
