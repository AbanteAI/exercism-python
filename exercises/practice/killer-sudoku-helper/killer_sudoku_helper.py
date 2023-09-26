def combinations(target, size, exclude):
    from itertools import combinations as comb

    valid_combinations = []
    for combination in comb(range(1, 10), size):
        if sum(combination) == target and all(num not in exclude for num in combination):
            valid_combinations.append(''.join(str(num) for num in combination))

    return sorted(valid_combinations)
