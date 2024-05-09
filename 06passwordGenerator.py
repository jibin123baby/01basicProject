#Password Generator Project
import random
from typing import List, Any

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator")
noLetters = 0
noNumbers = 0
noSymbols = 0

while True:
    try:
        noLetters = int(input("\n How Many letters would you like to have in this Password ..? Minimum 2 Characters"))
        if noLetters < 2:
            print("Please Choose to have at least 2 Letters")
            continue
    except ValueError:
        print("Please enter a Numeric Value, Greater that 2")
        continue
    else:
        break

while True:
    try:
        noNumbers = int(input("\n How Many Number you want in this Password ..? Minimum 2 Characters"))
        if noNumbers < 2:
            print("Please Choose to have at least 2 Letters")
            continue
    except ValueError:
        print("Please enter a Numeric Value, Greater that 2")
        continue
    else:
        break

while True:
    try:
        noSymbols = int(input("\n How Many Special characters you want in this Password ..? Minimum 2 Characters "))
        if noSymbols < 2:
            print("Please Choose to have at least 2 Letters")
            continue
    except ValueError:
        print("Please enter a Numeric Value, Greater that 2")
        continue
    else:
        break

passwordList = []

if noNumbers >= 2 and noSymbols >= 2 and noSymbols >= 2:
    for i in range(1, noLetters+1):
        passwordList.append(random.choice(letters))

    for i in range(1, noNumbers+1):
        passwordList.append(random.choice(numbers))

    for i in range(1, noSymbols+1):
        passwordList.append(random.choice(symbols))

    random.shuffle(passwordList)
    password = ''.join(passwordList)  # Converting List to a String
    print(f"Your Password is {password} \nDon't share it with anyone")
else:
    print("Please Choose to have at least 2 Letters, 2 Numbers and 2 Symbols")