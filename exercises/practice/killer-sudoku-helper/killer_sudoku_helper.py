def combinations(target, size, exclude):
    def is_valid_combination(combination):
        return sum(combination) == target and len(set(combination)) == size

    valid_combinations = []
    for i in range(10 ** size):
        combination = [int(digit) for digit in str(i).zfill(size)]
        if is_valid_combination(combination) and all(digit not in exclude for digit in combination):
            valid_combinations.append(combination)

    return sorted(valid_combinations)

    valid_combinations = []
    for i in range(10 ** size):
        combination = [int(digit) for digit in str(i).zfill(size)]
        if is_valid_combination(combination) and all(digit not in exclude for digit in combination):
            valid_combinations.append(combination)

    return sorted(valid_combinations)
