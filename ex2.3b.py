from collections import OrderedDict

"""Divides a sequence into blocks and and computes GC content for each block"""

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
