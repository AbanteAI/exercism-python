def hamming_distance(dna_strand_1, dna_strand_2):
    if len(dna_strand_1) > len(dna_strand_2):
        dna_strand_1, dna_strand_2 = dna_strand_2, dna_strand_1

    if len(dna_strand_1) != len(dna_strand_2):
        raise ValueError("DNA strands must be of equal length")

    return sum(1 for a, b in zip(dna_strand_1, dna_strand_2) if a != b)
