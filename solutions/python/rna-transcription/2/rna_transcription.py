def to_rna(dna_strand: str) -> str:
    return dna_strand.translate(dna_strand.maketrans('GCTA', 'CGAU'))
