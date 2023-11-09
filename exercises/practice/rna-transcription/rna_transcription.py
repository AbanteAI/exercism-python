def to_rna(dna_strand):
    """Return the RNA complement of a given DNA strand."""
    complement = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    return ''.join(complement[nucleotide] for nucleotide in dna_strand)
