def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    hamming_distance = 0
    for base_a, base_b in zip(strand_a, strand_b):
        if base_a != base_b:
            hamming_distance += 1

    return hamming_distance