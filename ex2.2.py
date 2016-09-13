#Open the file
with open('salmonella_spi1_region.fna', 'r') as f, open('salmonella_out.txt', 'w') as f_out:
    # Get all the lines
    lines = f.readlines()
    for row in lines:
        row.replace("\n", "")
    concat_salmonella = ''.join(lines)
    nolines_salmonella = concat_salmonella.replace("\n",'')
    f_out.write(nolines_salmonella)
