#Take a user input string and check if it is a palindrome (same forwards and backwards).

a = (input("Enter the String  "))
if (a == a[::-1]):
    print ("The String is  Palindrome")
else:
    print ("The String is not a Palindrome")