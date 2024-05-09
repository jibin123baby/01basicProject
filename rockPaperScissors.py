import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
lsFig = [rock, paper, scissors]
lsItm = ["Rock", "Paper", "Scissors"]
print("\n1. Rock", rock)
print("\n2. Paper", paper)
print("\n3. Scissors", scissors)
choice = int(input("What do you choose....?Choose one"))
compChoice = random.randint(1, 3)

if choice == compChoice:
    print(f"You choose {lsItm[choice-1]} {lsFig[choice-1]} "
          f"\nComputer Choose {lsItm[compChoice-1]} {lsFig[compChoice-1]} \nMatch Tied")
else:
    if choice == 1:
        if compChoice == 2:
            print(f"You choose {lsItm[choice-1]} {lsFig[choice - 1]} "
                  f"\nComputer Choose {lsItm[compChoice-1]} {lsFig[compChoice - 1]} \nYou Lose !!")
        else:
            print(f"You choose {lsItm[choice-1]} {lsFig[choice - 1]} "
                  f"\nComputer Choose {lsItm[compChoice-1]} {lsFig[compChoice - 1]} \nYou Won !!")

    elif choice == 2:
        if compChoice == 1:
            print(f"You choose {lsItm[choice-1]} {lsFig[choice - 1]} "
                  f"\nComputer Choose {lsItm[compChoice-1]} {lsFig[compChoice - 1]} \nYou Won !!")
        else:
            print(f"You choose {lsItm[choice-1]} {lsFig[choice - 1]} "
                  f"\nComputer Choose {lsItm[compChoice-1]} {lsFig[compChoice - 1]} \nYou Lose !!")
    else:
        if compChoice == 1:
            print(f"You choose {lsItm[choice-1]} {lsFig[choice - 1]} "
                  f"\nComputer Choose {lsItm[compChoice-1]} {lsFig[compChoice - 1]} \nYou Lose !!")
        else:
            print(f"You choose {lsItm[choice-1]} {lsFig[choice - 1]}"
                  f" \nComputer Choose {lsItm[compChoice-1]} {lsFig[compChoice - 1]} \nYou Won !!")
print("Thanks for Playing")