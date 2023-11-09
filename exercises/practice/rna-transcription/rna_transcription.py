def to_rna(dna_strand):
    """Return the RNA complement of a given DNA strand."""
    # Define the DNA to RNA complement mapping
    dna_to_rna = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    
    # Convert each DNA nucleotide to its RNA complement
    rna_strand = ''.join(dna_to_rna[nucleotide] for nucleotide in dna_strand)
    
    return rna_strand
