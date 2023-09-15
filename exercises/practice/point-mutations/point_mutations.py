def hamming_distance(dna_strand_1, dna_strand_2):
    if len(dna_strand_1) != len(dna_strand_2):
        raise ValueError("DNA strands must have equal length.")
    
    count = 0
    for i in range(len(dna_strand_1)):
        if dna_strand_1[i] != dna_strand_2[i]:
            count += 1
    
    return count
