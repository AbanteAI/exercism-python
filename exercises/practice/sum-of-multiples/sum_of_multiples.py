def sum_of_multiples(limit, multiples):
    return sum(set(num for multiple in multiples if multiple != 0 for num in range(multiple, limit, multiple)))