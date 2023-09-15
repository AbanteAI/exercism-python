def classify(number):
    aliquot_sum = sum([i for i in range(1, number) if number % i == 0])
    
    if aliquot_sum == number:
        return "Perfect"
    elif aliquot_sum > number:
        return "Abundant"
    else:
        return "Deficient"
    else:
        return "Deficient"
