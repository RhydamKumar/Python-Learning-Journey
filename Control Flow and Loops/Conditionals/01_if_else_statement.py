# if statement
height = int (input("Enter your height in cm: "))

if (height > 150):
    print("You are tall enough to ride the roller coaster!")

# if-else statement
age = int (input("Enter your age: "))

if (age > 18):
    print("You are old enough to ride vehicles!")
else:
    print("Sorry, you have to be older to ride vehicles.")

# if-elif-else statement
weight = int (input("Enter your weight in kg: "))
if (weight >= 100):
    print("Sorry, you are overweight. Please exercise more!")
elif (weight >= 70):
    print("Your body is healthy!")
elif (weight >= 50):
    print("Your body is normal weight.")
else:
    print("You are underweight. Please eat more nutritious food!")