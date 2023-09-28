def hamming_distance(dna_strand_1, dna_strand_2):
    if len(dna_strand_1) != len(dna_strand_2):
        raise ValueError("DNA strands must be of equal length")
    
    distance = 0
    for base1, base2 in zip(dna_strand_1, dna_strand_2):
        if base1 != base2:
            distance += 1
    
    return distance
