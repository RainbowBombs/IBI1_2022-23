#NOTE： I  read the sequences three in a group

import re  
# Importing the 're' module for regular expressions
seq=""  
# Initializing an empty string to store the DNA sequence
TGA_genes=open("C:/Users/DELL/OneDrive/桌面/lesson/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa","r")  
# Opening a file containing DNA sequences in FASTA format
save=open("C:/Users/DELL/OneDrive/桌面/lesson/TGA_genes.fa","w+")  
# Opening a file to save the DNA sequences with TGA codons
datalines=TGA_genes.readlines()  
# Reading all the lines from the input file
for line in datalines:  
# Looping through each line in the input file
    if re.match(">",line):  # Using a regular expression to check if the line starts with ">"
        name=line.split(" ")[0].strip(">")  
# Extracting the gene name from the line and removing "_mRNA" and ">" characters
        seq=""  
# Resetting the DNA sequence string for the new gene
        continue  
# Skipping to the next iteration of the loop
    seq+=line.strip("\n")  
# Appending the current line to the DNA sequence string
    for i in range(len(line)//3):  
# Looping through each codon in the line
        if re.match("TGA",line[3*i:3*i+3]):  
# Using a regular expression to check if the codon is "TGA"
            save.write(name+"\n"+seq+"\n")  
# Writing the gene name and its DNA sequence to the output file
save.close()  
# Closing the output file
TGA_genes.close()  
# Closing the input file