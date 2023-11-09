def to_rna(dna_strand):
    """Return the RNA complement of a given DNA strand."""
    # Define the DNA to RNA transcription mapping
    transcription_mapping = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    # Use a list comprehension to get the RNA complement for each nucleotide
    rna_strand = [transcription_mapping[nucleotide] for nucleotide in dna_strand]
    # Join the list of RNA nucleotides into a string and return it
    return ''.join(rna_strand)
