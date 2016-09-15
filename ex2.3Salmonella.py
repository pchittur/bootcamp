from collections import OrderedDict
import os

"""Divides a sequence into blocks and and computes GC content for each block"""
"""Also reads the salmonella_out file and writes to salmonella_mapped file"""

def gc_blocks (seq, block_size):
#Make the input string all upper case and then initiate a count and an empty list
    seq.upper()
    count = 0
    gc_list = []
    chunk_list = []
#Count increments the blocks - chunks with the block size
    for count in range(0, len(seq)//block_size):
        seq_chunk = seq[(count*block_size):(count*block_size + block_size)]
        gc_cont = seq_chunk.count('G') + seq_chunk.count('C')
        gc_frac = gc_cont/block_size
        gc_list.append(gc_frac)
#Makes a list of all the chunks
        chunk_list.append(seq_chunk)
#Dictionary of chunk:GC fraction pairs -- returns that
    pairs = OrderedDict(zip(chunk_list, gc_list))
    return pairs

def gc_map(seq, block_size, gc_thresh):
    unmapped_seq = gc_blocks(seq, block_size)
    modified_seq = []
    for keys in unmapped_seq:
        if unmapped_seq[keys] < gc_thresh:
            subseq = keys
            modified_seq.append(subseq.lower())
        else:
            subseq = keys
            modified_seq.append(subseq)
    return ''.join(modified_seq)

#The part where the file is opened and gc_map is performed on the data
#Modified code from previous to throw out the first line
with open('salmonella_spi1_region.fna', 'r') as f, open('salmonella_out.txt', 'w') as f_out:
    # Get all the lines
    lines = f.readlines()
    for i in range (1, len(lines)-1):
        lines[i].replace("\n", "")
    concat_salmonella = ''.join(lines[i:])
    nolines_salmonella = concat_salmonella.replace("\n",'')
    f_out.write(nolines_salmonella)
