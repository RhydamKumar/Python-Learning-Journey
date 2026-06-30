#Write a program that asks the user for a number and prints whether it is positive, negative, or zero.

a = float(input("Enter a number: "))

if a>0:
    print("The number is positive.")
elif a<0:
    print("The number is negative.")
else:
    print("The number is zero.")
