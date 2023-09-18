def hamming_distance(dna_strand_1, dna_strand_2):
    return sum(base1 != base2 for base1, base2 in zip(dna_strand_1, dna_strand_2))
