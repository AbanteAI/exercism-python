def count(strand, nucleotide):
    if nucleotide not in "ACGT":
        raise ValueError("Invalid nucleotide")
    return strand.count(nucleotide)


def nucleotide_counts(strand):
    if any(nucleotide not in "ACGT" for nucleotide in strand):
        raise ValueError("Invalid DNA sequence")
    return {"A": strand.count("A"), "C": strand.count("C"), "G": strand.count("G"), "T": strand.count("T")}
