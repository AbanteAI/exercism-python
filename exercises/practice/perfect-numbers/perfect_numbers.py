def classify(number):
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Number must be a positive integer.")
    aliquot_sum = sum(i for i in range(1, number) if number % i == 0)

    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    else:
        return "deficient"