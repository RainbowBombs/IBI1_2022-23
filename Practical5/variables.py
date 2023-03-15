#---------------3.1------------------
# Compare the absolute value of d and e, which can compare the distance that whether Rob	travel	further	to	Haining	or	Los	Angeles
a=-3.19
b=-118.24
c=116.39
d=abs(b-a) #abs is used because distance can't be negative
e=abs(c-a)
if e>d:
    print("Rob travel further to Haining")
if e<d:
    print("Rob travel further to Los Angeles")
#result Rob travel further to Haining

#---------------3.2---------------------
# test about Booleans
X=True
Y=False
W=X and Y
Z=X	or Y
#result:  W->False   Z->True  