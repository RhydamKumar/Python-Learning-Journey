#Write a program that counts how many vowels are in a given string.

text=input("Enter the scentence : ")
Sum = 0
Vowels = ['A','E','I','O','U','a','e','i','o','u']

for Char in text:
    if (Char in Vowels):
        Sum += 1

        
print ( "No. of Vowels in the scentence is : ", Sum)