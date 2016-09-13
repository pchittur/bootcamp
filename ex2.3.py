"""Divides a sequence into blocks and and computes GC content for each block"""

def gc_blocks (seq, block_size):
#Make the input string all upper case and then initiate a count and an empty list
    seq.upper()
    count = 0
    gc_list = []
#Count increments the blocks - chunks with the block size
    for count in range(0, len(seq)//block_size):
        seq_chunk = seq[(count*block_size):(count*block_size + block_size)]
        gc_cont = seq_chunk.count('G') + seq_chunk.count('C')
        gc_frac = gc_cont/block_size
        gc_list.append(gc_frac)
    return tuple(gc_list)
