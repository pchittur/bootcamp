import pytest
import bioinfo_dicts

def n_neg(seq):
    '''number of negative residues in a protein sequence'''

#convert to upper case
    seq=seq.upper()
#check for validity of the sequence
    for aa in seq:
        if aa not in bioinfo_dicts.aa.keys():
            raise RuntimeError(aa + "is not a valid amino acid")
#count Es and Ds and return count
    return seq.count('D') + seq.count('E')
