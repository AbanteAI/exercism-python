def count(strand, nucleotide):
    if nucleotide not in "ACGT":
        raise ValueError("Invalid nucleotide")
    return strand.count(nucleotide)


def nucleotide_counts(strand):
    if any(c not in "ACGT" for c in strand):
        raise ValueError("Invalid DNA strand")
    return {nucleotide: count(strand, nucleotide) for nucleotide in "ACGT"}
