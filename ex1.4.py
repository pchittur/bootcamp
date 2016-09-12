#part that gets the input and decides RNA or DNA
my_sequence = input("Please enter your sequence: ")
material = input("Please enter DNA or RNA: ")
while material != 'DNA' and material != 'RNA':
    print ("That is not a valid material. Please enter material again: ")
    material = input('')

#part that takes the sequence and reverses it
rev_sequence = [my_sequence[::-1]]

#part that writes the opp base
def get_rev_complement(str, material):
    str = str.replace('C','g')
    str = str.replace('G','C')
    if material == 'RNA':
        str = str.replace('A', 'u')
    else:
        str = str.replace('A','t')
    str = str.replace('T','A')
    str = str.replace('U','A')
    return str

rev_complement = get_rev_complement(str(rev_sequence), material=material)
print (str(rev_complement).upper())
