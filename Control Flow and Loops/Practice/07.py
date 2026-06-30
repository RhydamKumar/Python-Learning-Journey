#Print the multiplication table of a number (entered by user).

a = int ( input("Enter a number to print its multiplication table: ") )
for i in range (1,11):
    b = a * i
    print ( a, "x", i , "=", b)