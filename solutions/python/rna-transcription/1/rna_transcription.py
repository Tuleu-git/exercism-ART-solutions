def to_rna(dna_strand: str) -> str:
    formatting = str.maketrans('GCTA', 'CGAU')
    return dna_strand.translate(formatting)
