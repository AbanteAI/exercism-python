def hamming_distance(dna_strand_1, dna_strand_2):
    """Calculate the Hamming distance between two DNA strands.
    
    Args:
        dna_strand_1 (str): The first DNA strand.
        dna_strand_2 (str): The second DNA strand.
        
    Returns:
        int: The Hamming distance between the DNA strands.
    """
    # Calculate the distance only up to the length of the shorter strand
    min_length = min(len(dna_strand_1), len(dna_strand_2))
    return sum(n1 != n2 for n1, n2 in zip(dna_strand_1[:min_length], dna_strand_2[:min_length]))
