def to_rna(dna_strand):
    dna_to_rna = {"G": "C", "C": "G", "T": "A", "A": "U"}
    rna_strand = "".join([dna_to_rna[nucleotide] for nucleotide in dna_strand])
    return rna_strand
