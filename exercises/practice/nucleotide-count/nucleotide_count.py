def count(strand, nucleotide):
    if nucleotide not in "ACGT":
        raise ValueError("Invalid nucleotide")
    return strand.count(nucleotide)


def nucleotide_counts(strand):
    if any(char not in "ACGT" for char in strand):
        raise ValueError("Invalid strand")
    return {"A": strand.count("A"), "C": strand.count("C"), "G": strand.count("G"), "T": strand.count("T")}
