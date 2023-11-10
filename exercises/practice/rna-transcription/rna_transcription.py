def to_rna(dna_strand):
    # Define the DNA to RNA transcription map
    transcription_map = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    
    # Convert the DNA strand to its RNA complement
    rna_strand = ''.join(transcription_map[nucleotide] for nucleotide in dna_strand)
    
    return rna_strand