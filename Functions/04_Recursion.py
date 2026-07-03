# fibinacci series (best example of recursion)
def fib(n):
    if n==0 or n==1:
        return n

    return fib (n-2) +fib (n-1)


for i in range (0,10):    #printing series from 1 to 10
    print (fib(i))