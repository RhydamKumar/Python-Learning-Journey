print("Welcome to the Kingdom!")
Kingdom = int(input("Enter a number between 1 and 10: "))

match Kingdom:
    case 7:
        print("You will be the King.")
    case 5:
        print("You will be the jack")
    case 3:
        print("You will be the knight.")
    case 8:
        print("You will be the theif.")
    case _:
        print("You wil be the part of army.")