CODON_PROTEIN_MAP = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": "STOP",
    "UAG": "STOP",
    "UGA": "STOP"
}

def proteins(strand):
    codons = [strand[i:i+3] for i in range(0, len(strand), 3)]
    protein_sequence = []
    for codon in codons:
        protein = CODON_PROTEIN_MAP[codon]
        if protein == "STOP":
            break
        protein_sequence.append(protein)
    return protein_sequence
