s = "Rhydam Kumar"
a = "vinod kumar"

#s = "R" [we cant change the string as it is immutable]

print (len(s)) #length of the string
print (s.upper()) #converts to uppercase
print (s.lower()) #converts to lowercase
print (a.capitalize()) #converts to capitalized form
print (a.title()) #converts to title case


name = "   Rhydam Kumar   "
print (name.strip()) #removes leading and trailing spaces (both left and right)
print (name.lstrip()) #removes leading (left one only) spaces
print (name.rstrip()) #removes trailing (Right one only) spaces

text = "freindship is fun and fun and fun"
print (text.count("fun")) #counts the number of occurrences of a substring
print (text.find("and")) #finds the first occurrence of a substring and returns its index. If not found, returns -1
print (text.replace("fun", "awesome")) #replaces a substring with another substring

text2 = "Apples, Bananas, Oranges"
print(text2.split(", ")) #splits the string into a list 
mylist = ["Avocado", "Cherries", "Grapes"]
print(", ".join(mylist)) #joins the elements of a list into a single string.

c = "Rhydam2004"
# only says True or False
print(c.isalnum()) #checks if all characters in the string are alphanumeric (letters and numbers)
print(c.isalpha()) #checks if all characters in the string are alphabetic (letters only)
print(c.isdigit()) #checks if all characters in the string are digits (numbers only)
print(c.isspace()) #checks if all characters in the string are whitespace characters (spaces, tabs, newlines, etc.)

