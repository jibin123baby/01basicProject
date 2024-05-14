
"""

1. Welcome the User
2. Randomly Select Two Items to Compare
3. Display the Items (2 Items from the List)
4. Ask the User to Guess the Winner
5. If the user is right, repeat step 2 , 3 and 4 else, display the Game over message with User's score

"""
import random
from art import vs_art, game_logo
from gamedata import game_data


def generate_items(index):
    """
        This function will generate a list of two items to Compare
    :return: list of two items to Compare
    """
    if index < 0:
        item_a = random.choice(game_data)
    else:
        item_a = game_data[index]
    item_b = random.choice(game_data)
    while item_a == item_b:
        item_b = random.choice(game_data)

    return [item_a, item_b]


def display_items(items_list):
    """
    This function will display two items to compare
    :param items_list:
    :return: User choice of the items
    """
    print(f"Compare A: {items_list[0]["name"]}, a {items_list[0]["description"]}, from {items_list[0]["country"]}")
    print(f"{vs_art}")
    print(f"Against B: {items_list[1]["name"]}, a {items_list[1]["description"]}, from {items_list[1]["country"]}")
    choice = input("Who has more followers ? Type 'A'  or 'B': ").lower()
    if choice == 'a':
        return 'a'
    elif choice == 'b':
        return 'b'
    else:
        print("Invalid Input. Please Try again")
        return 'invalid'


def check_status(result, items_list):
    """
    This function will check the followers of each choice and choose a winner
    :param result:
    :param items_list:
    :return:
    """
    if items_list[0]["follower_count"] > items_list[1]["follower_count"]:
        return result == 'a'
    else:
        return result == 'b'

    # if result == 'a':
    #     if items_list[0]["follower_count"] > items_list[1]["follower_count"]:
    #         return [True,  gamedata.game_data.index(items_list[0])]
    #     else:
    #         return [False,-1]
    # if result == 'b':
    #     if items_list[0]["follower_count"] < items_list[1]["follower_count"]:
    #         return [True,  gamedata.game_data.index(items_list[1])]
    #     else:
    #         return [False, -1]


def get_index(result, items_list):
    """
        This function will get the index of the item choose by the user
    :param result: Item choose by the user
    :param items_list: Two items that are displayed for comparison
    :return: Index of the item chosen by the user
    """
    if result == 'a':
        return game_data.index(items_list[0])
    else:
        return game_data.index(items_list[1])


def play_game():
    print(game_logo)
    player_status = True
    score = 0
    # item_b = random.choice(game_data)
    index = -1
    while player_status:

        # item_a = item_b
        # item_b = random.choice(game_data)
        # while item_a == item_b:
        #     item_b = random.choice(game_data)

        # items_to_compare_list = [item_a, item_b]

        items_to_compare_list = generate_items(index)
        result = display_items(items_to_compare_list)
        if result == 'invalid':
            return
        player_status = check_status(result, items_to_compare_list)

        if player_status:
            score = score + 1
            print(f"Your are right. Your score is {score}")
            index = get_index(result, items_to_compare_list)
            print("-------------------------------------------------")
    if not player_status:
        print("-------------------------------------------------")
        print(f"Sorry That's wrong. Your Final Score is {score}")


play_game()
