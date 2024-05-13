import random

EASY_CHANCES = 10
HARD_CHANCES = 5
SLIGHT_VALUE = 5


def generate_number():
    return random.randint(1, 100)


def checkguess(user_guess, computer_guess):
    if user_guess == computer_guess:
        return "pass"
    elif user_guess > computer_guess:
        if user_guess - computer_guess <= SLIGHT_VALUE:
            return "sh"
        else:
            return "th"
    elif user_guess < computer_guess:
        if computer_guess - user_guess <= SLIGHT_VALUE:
            return "sl"
        else:
            return "tl"


def print_message(status):
    if status == 'th':
        print("You Guess is Too high")
    elif status == 'tl':
        print("You Guess is Too Low")
    elif status == 'sh':
        print("You Guess is Slightly high")
    elif status == 'sl':
        print("You Guess is Slightly Low")
    elif status == 'pass':
        print("Wow...... Your Guess is Accurate. Congrats....")


def play_game():
    print("Welcome to the Number Guessing Game")
    print("----------------------------------------------")
    print("I will guess a number between 1 and 100")
    computer_guess = generate_number()
    print(computer_guess)

    difficulty = input("Please Choose the level of difficulty.\n1. Easy\n2. Hard\n").lower()
    if difficulty == '1' or difficulty == 'easy':
        no_attempts = EASY_CHANCES
    else:
        no_attempts = HARD_CHANCES

    status = ''
    for i in range(0, no_attempts):
        print(f"Chances Remaining is {no_attempts - i}")
        if i == 0:
            user_guess = int(input(f"Make you first Guess: "))
        else:
            user_guess = int(input(f"Make Another Guess: "))
        status = checkguess(user_guess, computer_guess)
        print_message(status)
        print("------------------------------------------------------------------")
        if status == 'pass':
            return    # It will end the Function
    if status != 'pass':
        print("You Don't have any more Chances")
        print(f"Correct Guess was {computer_guess}")


play_again = True
while play_again:
    play_game()
    user_input = input("Do you Want to Play Again .\n1. Yes\n2. No\n").lower()
    if user_input == '1' or user_input == 'yes':
        play_again = True
    else:
        play_again = False
