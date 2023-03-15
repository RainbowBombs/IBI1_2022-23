# What does this piece of code do?
# Answer:choose the maximum one from 10 randomn integer figures which range from 1 to 99(not include 100)
# and print it.
# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0
stored_random_number=0
while progress<10:  # this line tells us it will choose 10 figures（when progress add up to 10, the "while" will stop）
	progress+=1
	n = randint(1,100) # n is between 1 to 99
	if n > stored_random_number:  #this follow two lines tell us it save the largest name
		stored_random_number = n

print(stored_random_number) # print the largest n