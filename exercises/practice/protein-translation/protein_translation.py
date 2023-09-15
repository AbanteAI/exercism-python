def proteins(strand):
    codons = [strand[i:i+3] for i in range(0, len(strand), 3)]
    protein = []
    for codon in codons:
        if codon == "AUG":
            protein.append("Methionine")
        elif codon in ["UUU", "UUC"]:
            protein.append("Phenylalanine")
        elif codon in ["UUA", "UUG"]:
            protein.append("Leucine")
        elif codon in ["UCU", "UCC", "UCA", "UCG"]:
            protein.append("Serine")
        elif codon in ["UAU", "UAC"]:
            protein.append("Tyrosine")
        elif codon in ["UGU", "UGC"]:
            protein.append("Cysteine")
        elif codon == "UGG":
            protein.append("Tryptophan")
        elif codon in ["UAA", "UAG", "UGA"]:
            break
    return protein
