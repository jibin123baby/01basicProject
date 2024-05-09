print("Welcome to Treasure Island.\nYour Mission is to find the treasure")
choice = input("Left or Right ? \n1. Right\n2. Left ")
if choice == '1':
    print("Game Over")
else:
    choice = input("Swim or Wait ? \n1. Swim\n2. Wait ")
    if choice == '1':
        print("Game Over")
    else:
        choice = input("Which door ? \n1. Red\n2. Blue\n3. Yellow ")
        if choice == '3':
            print("You Win")
        else:
            print("Game Over")