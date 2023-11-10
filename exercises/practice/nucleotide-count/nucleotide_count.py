def count(strand, nucleotide):
    if nucleotide not in 'ACGT':
        raise ValueError("Invalid nucleotide")
    return strand.count(nucleotide)

def nucleotide_counts(strand):
    if not all(nucleotide in 'ACGT' for nucleotide in strand):
        raise ValueError("Invalid nucleotide in strand")
    return {nucleotide: strand.count(nucleotide) for nucleotide in 'ACGT'}