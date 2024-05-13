"""
    This program takes input from a number of bidders and
    Compare their values. Then Select the person with the highest bid
    as the winner
"""
import os


def clear():
    # for Windows
    if os.name == 'nt':
        _ = os.system('cls')

    # Mac or Linux (aka posix)
    else:
        _ = os.system('clear')


'''
    This method will compare the bids and Select the highest Bidder
    If there are two same bids, First bidder will be the winner
'''


def choose_highest(bid_dict1):
    high_bid = 0.0
    highest_bidder = ""
    for key in bid_dict1:
        if high_bid < bid_dict1[key]:
            high_bid = bid_dict1[key]
            highest_bidder = key
    print(f"The Winner is {highest_bidder} and the bid is {high_bid}")


more_bidders = True
bid_dict = {}


while more_bidders:
    name = input("Please Enter your name: ")
    print(f"Hello {name}, Welcome to the Bidding Game")
    print("---------------------------------------------\n")
    bid_amt = float(input("Enter the Bid Amount: "))
    bid_dict[name] = bid_amt
    choice = (input("Is there More Bidders ..?\n1. Yes\n2. No\n")).lower()
    if choice == '1' or choice == 'yes':
        more_bidders = True
    else:
        more_bidders = False

    clear()    # To clean the terminal

print(bid_dict)
choose_highest(bid_dict)
print("Thanks Everyone")
