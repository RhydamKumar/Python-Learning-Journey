#Default arguments

def add (a,b,plus=0):
    x= a+b+plus
    return x

c = add (2,3,5) # value of plus is passed as 5
print(c)

d = add (2,3) # default value for plus is used
print(d)

#keyword arguments
e = add (a=2, b=3, plus=5) # When we show which value is for which parameter , that is called keyword arguments. We can also change the order of the parameters.
print(e)
