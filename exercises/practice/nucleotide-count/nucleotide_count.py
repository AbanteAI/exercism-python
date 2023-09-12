def count(strand, nucleotide):
    if nucleotide not in "ATCG":
        raise ValueError("Invalid nucleotide.")
    return strand.count(nucleotide)

def nucleotide_counts(strand):
    return {
        "A": count(strand, "A"),
        "T": count(strand, "T"),
        "C": count(strand, "C"),
        "G": count(strand, "G"),
    }