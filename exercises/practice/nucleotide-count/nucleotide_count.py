def count(strand, nucleotide):
    if nucleotide not in "ACGT":
        raise ValueError("Invalid nucleotide")
    return strand.count(nucleotide)


def nucleotide_counts(strand):
    if any(nucleotide not in "ACGT" for nucleotide in strand):
        raise ValueError("Invalid DNA sequence")
    return {
        "A": count(strand, "A"),
        "C": count(strand, "C"),
        "G": count(strand, "G"),
        "T": count(strand, "T"),
    }
