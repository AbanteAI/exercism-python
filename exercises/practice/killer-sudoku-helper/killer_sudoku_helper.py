def combinations(target, size, exclude):
    from itertools import combinations

    # Generate all possible combinations of the given size
    all_combinations = combinations(range(1, 10), size)

    # Filter out combinations that do not add up to the target sum or contain excluded digits
    valid_combinations = [
        list(combo) for combo in all_combinations
        if sum(combo) == target and not any(digit in exclude for digit in combo)
    ]
    ]

    # Sort the combinations
    valid_combinations.sort()

    return valid_combinations