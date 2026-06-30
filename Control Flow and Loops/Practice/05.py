# # Write a program using match case that simulates a simple calculator.

# Ask the user for two numbers and an operation (+, -, *, /).
# Perform the operation using match case.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
select_operator = input("Enter an operation (+, -, *, /): ")

match select_operator:
    case "+":
        result = a + b
        print("Addition=",result)
    case "-":
        result = a - b
        print("Subtraction=",result)
    case "*":
        result = a * b
        print("Multiplication=",result)
    case "/":
        if b != 0:
            result = a / b
            print("Division=",result)
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid operation. Please select one of +, -, *, /.")