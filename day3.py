print("Welcome to Treasure island.")
print("Your mission is to find the treasure.")

choice1 = input("You're at a crossroads, where do you go? Type either 'left' or 'right' ")

if choice1 == "right":
    print("Game over")
elif choice1 == "left":
    choice2 = input("You approach the sea. Do you wait or swim? ")
    if choice2 == "swim":
        print("Game over")
    elif choice2 == "wait":
        print("A boat arrives with three entrances. What door do you walk through?")
        choice3 = input("Red, Blue, or Yellow? ")
        if choice3 == "Red":
            print("Game over")
        elif choice3 == "Blue":
            print("Game over")
        elif choice3 == "Yellow":
            print("You win!")