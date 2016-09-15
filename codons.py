# codon = input('Enter your codon: ')
# codon_list = ['UAA', 'UAG', 'UGA']
# if codon == 'AUG':
#     print('This codon is the start codon.')
# elif codon in codon_list:
#     print('This is a stop codon')
# else:
#     print('This codon is neither a start nor stop codon')

#find the first ATG and then skip i = i+3

"""Code below DOES NOT WORK."""
def find_codon_lesson6(codon, seq):
    """Find a specified codon with a given sequence."""
    i = 0
    # Scan sequence until we hit the start codon or the end of the sequence
    while seq[i:i+3] != 'ATG' and i < len(seq):
        i += 1
    if i == len(seq):
        return -1
    return i

# first_atg = find_codon_lesson6('ATG', 'ATGGAGAACAACGAAGCCCCCTCCCCCTCGGGATCCAACAACAACGAGAACAA\
# CAATGCAGCCCAGAAGAAGCTGCAGCAGACCCAAGCCAAGGTGGACGAGGTGGTCGGGATTATGCGTGTGAACG\
# TGGAGAAGGTCCTGGAGCGGGACCAGAAGCTATCGGAACTGGGCGAGCGTGCGGATCAGCTGGAGCAGGGAG\
# CATCCCAGTTCGAGCAGCAGGCCGGCAAGCTGAAGCGCAAGCAATGGTGGGCCAACATGAAGATGATGATCATT\
# CTGGGCGTGATAGCCGTTGTGCTGCTCATCATCGTTCTGGTGTCGCTTTTCAATTGA')
