def hamming_distance(dna_strand_1, dna_strand_2):
    """Calculate the Hamming distance between two DNA strands.

    The Hamming distance is only defined for sequences of equal length.
    This function assumes both DNA strands are of equal length.

    Args:
        dna_strand_1 (str): The first DNA strand.
        dna_strand_2 (str): The second DNA strand.

    Returns:
        int: The Hamming distance between the DNA strands.
    """
    return sum(n1 != n2 for n1, n2 in zip(dna_strand_1, dna_strand_2))
