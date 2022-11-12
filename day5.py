import random

print("Welcome to the password generator")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letter_input = int(input("How many letters do you want in your password?\n "))
numbers_input = int(input("How many numbers do you want in your password?\n "))
symbols_input = int(input("How many symmbols do you want in your password?\n "))

total_characters = letter_input + numbers_input + symbols_input

letter_portion = []
number_portion = []
symbol_portion = []

for i in range(0, letter_input):
    letter_portion.append(random.choice(letters))

for j in range(0, numbers_input):
    number_portion.append(random.choice(numbers))

for k in range(0, symbols_input):
    symbol_portion.append(random.choice(symbols))

letter_portion.extend(number_portion)
letter_portion.extend(symbol_portion)

password_final = []

for l in range(0, total_characters):
    password_final.append(random.choice(letter_portion))

your_password = ''
for char in password_final:
    your_password += char

print(f"Your randomly generated password is {your_password}, have a great day.")