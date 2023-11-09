def count(strand, nucleotide):
    if not set(strand).issubset({'A', 'C', 'G', 'T'}) or nucleotide not in 'ACGT':
        raise ValueError("Invalid nucleotide")
    return strand.count(nucleotide)


def nucleotide_counts(strand):
    if not set(strand).issubset({'A', 'C', 'G', 'T'}):
        raise ValueError("Invalid nucleotide in strand")
    return {nucleotide: strand.count(nucleotide) for nucleotide in 'ACGT'}
