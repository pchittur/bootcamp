#part that gets the input and decides RNA or DNA
my_sequence = input("Please enter your sequence: ")
material = input("Please enter DNA or RNA: ")
while material != 'DNA' and material != 'RNA':
    print ("That is not a valid material. Please enter material again: ")
    material = input('')

#part that takes the sequence and reverses it
rev_sequence = []
for i in range(len(my_sequence)-1,0,-1):
    rev_sequence.append(my_sequence[i])

#part that writes the opp base
def get_rev_complement(str, material):
    rev_complement = []
    for base in str:
        if base in 'Aa':
            if material == 'RNA':
                rev_complement.append('U')
            else:
                rev_complement.append('T')
        elif base in 'TtUu':
            rev_complement.append('A')
        elif base in 'Cc':
            rev_complement.append('G')
        else:
            rev_complement.append('C')
    return rev_complement

rev_complement = get_rev_complement(rev_sequence, material=material)
print (''.join(rev_complement))
