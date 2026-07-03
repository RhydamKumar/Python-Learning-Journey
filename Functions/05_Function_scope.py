def sum(a,b):
    #a and b are local variables, they are only accessible within the function
    c = a+b
    return c 
    
z = 21 # z is a global variable, it can be accessed anywhere in the code

print (z)
print (sum(10,8))
