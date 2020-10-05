codonProtein = {
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
}

stopCodons = ["UAA", "UAG", "UGA"]


def chunk(string, chars):
    return [string[i : i + chars] for i in range(0, len(string), chars)]


class Protein:
    def __init__(self, codon):
        if codon not in codonProtein:
            raise Exception("INVALID CODON")

        self.codon = codon
        self.name = codonProtein[codon]


class AminoAcid:
    def __init__(self, codons):
        self.proteins = []
        for codon in codons:
            if codon in stopCodons:
                break
            self.proteins.append(Protein(codon))


def proteins(strand):
    chunks = chunk(strand, 3)
    aminoAcid = AminoAcid(chunks)
    return [p.name for p in aminoAcid.proteins]
