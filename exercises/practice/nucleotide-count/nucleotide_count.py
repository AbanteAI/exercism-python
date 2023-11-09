def count(strand, nucleotide):
    if nucleotide not in 'ACGT':
        raise ValueError("Invalid nucleotide.")
    if not set(strand).issubset(set('ACGT')):
        raise ValueError("Strand contains invalid nucleotides.")
    return strand.count(nucleotide)


def nucleotide_counts(strand):
    if not set(strand).issubset(set('ACGT')):
        raise ValueError("Strand contains invalid nucleotides.")
    return {nucleotide: strand.count(nucleotide) for nucleotide in 'ACGT'}
