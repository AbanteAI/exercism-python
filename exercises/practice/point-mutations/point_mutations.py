def hamming_distance(dna_strand_1, dna_strand_2):
    """Calculate the Hamming distance between two DNA strands up to the length of the shorter strand.
    
    Args:
        dna_strand_1 (str): The first DNA strand.
        dna_strand_2 (str): The second DNA strand.

    Returns:
        int: The Hamming distance between the DNA strands.
    """
    shortest_length = min(len(dna_strand_1), len(dna_strand_2))
    return sum(n1 != n2 for n1, n2 in zip(dna_strand_1[:shortest_length], dna_strand_2[:shortest_length]))
