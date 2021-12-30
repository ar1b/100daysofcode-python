import random

print('Welcome to the Rock, Paper, and Scissors.')
choice = str(input('Make your choice. Rock, Paper, or Scissors? '))

comp_choice = random.randint(0,2)

if comp_choice == 0:
    comp_choice = 'Rock'
elif comp_choice == 1:
    comp_choice = 'Paper'
elif comp_choice == 2:
    comp_choice = 'Scissors'

if choice == comp_choice:
    print("It's a draw!")
elif choice == 'Rock' and comp_choice == 'Paper':
    print("You win!")
elif choice == 'Paper' and comp_choice == 'Rock':
    print("You win!")
elif choice == 'Scissors' and comp_choice == 'Rock':
    print("You win!")
else:
    print("The computer won! you lose!")
