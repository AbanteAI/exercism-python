def hamming_distance(dna_strand_1, dna_strand_2):
    if len(dna_strand_1) != len(dna_strand_2):
        raise ValueError("DNA strands must have equal length")
    
    return sum(1 for a, b in zip(dna_strand_1, dna_strand_2) if a != b)
        raise ValueError("DNA strands must have equal length")
    
    return sum(1 for a, b in zip(dna_strand_1, dna_strand_2) if a != b)
