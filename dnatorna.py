"""Convert DNA to RNA"""

def rna(seq):
    """Convert DNA sequence to RNA. The returned string is all upper case."""
    seq = seq.upper()
    return seq.replace('T', 'U')
