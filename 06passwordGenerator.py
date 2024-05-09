#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator")

noLetters = int(input("\n How Many letters would you like to have in this Password ..? "))
noNumbers = int(input("\n How Many Number you want in this Password ..? "))
noSymbols = int(input("\n How Many Special characters you want in this Password ..? "))

password = ""

for i in range(1, noLetters+1):
    password = password + random.choice(letters)
for i in range(1, noNumbers+1):
    password = password + random.choice(numbers)
for i in range(1, noSymbols+1):
    password = password + random.choice(symbols)

print(f"Your Password is {password} \n Don't share it with anyone")