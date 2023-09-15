def count(strand, nucleotide):
    if nucleotide not in "ACGT":
        raise ValueError("Invalid nucleotide")
    return strand.count(nucleotide)


def nucleotide_counts(strand):
    if any(char not in "ACGT" for char in strand):
        raise ValueError("Invalid strand")
    return {nucleotide: count(strand, nucleotide) for nucleotide in "ACGT"}
