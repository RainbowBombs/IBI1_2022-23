import re  # Importing the 're' module for regular expressions
seq = "ATGCAATCGACTACGATCTGAGAGGGCCTAA"  # Defining a DNA sequence
if re.match("ATG",seq):  # Using a regular expression to check if the sequence starts with "ATG"
    list_number=re.findall(r"TAA|TAG|TGA",seq)  # Finding all occurrences of "TAA", "TAG", or "TGA" in the sequence
    print(len(list_number))  # Printing the count of occurrences
else: 
    print(0)  # If the sequence doesn't start with "ATG", printing 0


# the following is a code can read 3 words in a group
‘’‘if re.match("ATG",SEQ):
    for i in range(len(SEQ)//3):
        if re.match(r"TAA|TAG|TGA",SEQ[3*i:3*i+3]):
            number+=1
    print(number)
else: 
    print(0)’‘’    