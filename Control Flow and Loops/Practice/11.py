#Write a program that keeps asking the user to enter a password until they enter the correct one.

correct_password = "admin123"
a= input("Enter the password to login: ")
while a!=correct_password:
    print("Incorrect password. Please try again.")
    a= input("Enter the password to login: ")
print("Login successful!")