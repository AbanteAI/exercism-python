def count(strand, nucleotide):
    if not set(strand).issubset({'A', 'C', 'G', 'T'}) or nucleotide not in {'A', 'C', 'G', 'T'}:
        raise ValueError("Invalid nucleotide in strand")
    return strand.count(nucleotide)


def nucleotide_counts(strand):
    if not set(strand).issubset({'A', 'C', 'G', 'T'}):
        raise ValueError("Invalid nucleotide in strand")
    return {
        'A': strand.count('A'),
        'C': strand.count('C'),
        'G': strand.count('G'),
        'T': strand.count('T')
    }
