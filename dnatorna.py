"""Convert DNA to RNA"""

def rna(seq):
    """Convert DNA sequence to RNA"""
    seq = seq.upper()
    return seq.replace('T', 'U')
