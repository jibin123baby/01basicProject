#Step 1
import random
import words
import hangManArt

#word_list = ["aardvark", "baboon", "camel"]
word_list = words.word_list

print("Welcome to the HangMan Game")
print(hangManArt.logo)
print("\n")
chosen_word = random.choice(word_list)
#print(chosen_word)

guessedWord = []
for i in range(0, len(chosen_word)):
    guessedWord.append("-")
print(guessedWord)


def checkword(guessedword1, chosen_word1, guess1):
    i = 0
    for letter in chosen_word1:
        if letter == guess1:
            guessedword1[i] = letter
        i = i + 1
    print(guessedword1)


noChances = len(hangManArt.stages)

while noChances >= 0:
    if noChances == 0 and ''.join(guessedWord) != chosen_word:
        print("You Lost")
        print(f"Correct Word Was {chosen_word}")
        print(f"Guessed Word {guessedWord}")
        break
    elif ''.join(guessedWord) == chosen_word:
        print("You Won")
        print(f"Correct Word: {chosen_word}")
        print(f"Guessed Word: {guessedWord}")
        break
    elif ''.join(guessedWord) != chosen_word:
        guess = input("Guess a Letter: ")
        checkword(guessedWord, chosen_word, guess)
        if ''.join(guessedWord) != chosen_word:
            print(hangManArt.stages[noChances-1])
    else:
        print("Unexpected Situation")
        break
    noChances = noChances -1
