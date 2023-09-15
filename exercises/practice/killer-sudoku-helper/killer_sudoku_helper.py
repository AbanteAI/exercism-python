def combinations(target, size, exclude):
    valid_combinations = []
    # Generate all combinations of digits from 1 to 9
valid_combinations = []
# Generate all combinations of digits from 1 to 9
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            combination = [i, j, k]
            # Check if the combination is valid
            if sum(combination) == target and len(combination) == size and set(combination).isdisjoint(exclude):
                valid_combinations.append(combination)
# Sort the combinations
valid_combinations.sort()
return valid_combinations if valid_combinations else []