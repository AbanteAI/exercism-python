def hamming_distance(dna_strand_1, dna_strand_2):
    # Initialize a counter for the differences
    differences = 0

    # Iterate over the two DNA strands
    for base1, base2 in zip(dna_strand_1, dna_strand_2):
        # If the bases are different, increment the counter
        if base1 != base2:
            differences += 1

    # Return the total number of differences
    return differences