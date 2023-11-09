def count(strand, nucleotide):
    if not set(strand).issubset({'A', 'C', 'G', 'T'}):
        raise ValueError("Invalid nucleotide in strand")
    if nucleotide not in {'A', 'C', 'G', 'T'}:
        raise ValueError("Invalid nucleotide")
    return strand.count(nucleotide)


def nucleotide_counts(strand):
    if not set(strand).issubset({'A', 'C', 'G', 'T'}):
        raise ValueError("Invalid nucleotide in strand")
    return {'A': strand.count('A'), 'C': strand.count('C'), 'G': strand.count('G'), 'T': strand.count('T')}
