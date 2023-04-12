import re  
# Importing the 're' module for regular expressions
number=0  
# Initializing a counter for the number of occurrences
seq=""  
# Initializing an empty string to store the DNA sequence
user_choice=input("give me a type of stop codons(TAA, TAG or TGA):")  
# Prompting the user for input on the type of stop codon
given_genes=open("C:/Users/DELL/OneDrive/桌面/lesson/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa","r")  
# Opening a file containing DNA sequences in FASTA format
save=open(f"C:/Users/DELL/OneDrive/桌面/lesson/{user_choice}_genes.fa","w")  
# Opening an output file to save the genes with the user-specified stop codon
datalines=given_genes.readlines()  
# Reading all the lines from the input file
for line in datalines:  
# Looping through each line in the input file
    if re.match(">",line):  
# Using a regular expression to check if the line starts with ">"
        if number>0:  
# Writing the gene name and the count of occurrences to the output file for the previous gene
            save.write(name+"  "+str(number) +"\n")
            number=0  
# Resetting the occurrence counter for the new gene
        name=line.split(" ")[0].strip(">")  
# Extracting the gene name from the line and removing any extra characters
        seq=""  
# Resetting the DNA sequence string for the new gene
    seq+=line.strip("\n")  
# Appending the current line to the DNA sequence string
    for i in range(len(line)//3):  
# Looping through each codon in the line
        if re.match(user_choice,line[3*i:3*i+3]):  
# Using a regular expression to check if the codon matches the user-specified stop codon
            number+=1  
# Incrementing the occurrence counter for the current gene
save.close()  
# Closing the output file
given_genes.close()  
# Closing the input file