#For each value of n in the range from 1 to 5, do the following:
#Calculate h using the formula 2n(2*n-1)/2
#Convert h to an integer using the int() function
#Print the value of h to the console.

for n in range(1,6): # this tell us it will compute n from 1 to 5
    h=2*n*(2*n-1)/2
    print(int(h)) # if int() isn't used, it will print figure like 1.0 and 6.0.
#result:
#1
#6
#15
#28
#45
