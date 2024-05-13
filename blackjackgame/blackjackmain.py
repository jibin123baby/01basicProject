"""
This Program Allows Users to Play the Game of Black Jack

"""

'''
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

'''
import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
customer_cards = []
dealer_cards = []
ace = 11


def score_calc(cards_list):
    score = 0
    # if user == 'customer':
    #     score = sum(customer_cards)
    # else:
    #     score = sum(dealer_cards)
    # return score
    return sum(cards_list)


def add_cards(rounds, is_pass):
    if rounds == 1:
        for i in range(2):
            customer_cards.append(random.choice(cards))
            dealer_cards.append(random.choice(cards))
    else:
        if is_pass:
            if score_calc(dealer_cards) <= 17:
                dealer_cards.append(random.choice(cards))
        else:
            customer_cards.append(random.choice(cards))
            if score_calc(customer_cards) <= 21:
                dealer_cards.append(random.choice(cards))


def score_check(customer_score, dealer_score, is_pass1):

    if customer_score == 21:
        if customer_score == dealer_score:
            return "draw"
        return "customer"
    elif dealer_score == 21:
        return "dealer"

    elif customer_score > 21:
        if dealer_score > customer_score:
            return "customer"
        if ace in customer_cards:
            index = customer_cards.index(ace)
            customer_cards[index] = 1
            score_check(score_calc(customer_cards), dealer_score, is_pass1)
        else:
            return "dealer"
    elif dealer_score > 21:
        return "customer"
    elif customer_score > 21 and customer_score == dealer_score:
        return "draw"
    elif is_pass1:
        print("Match is Over")
        if customer_score > dealer_score:
            return "customer"
        elif customer_score < dealer_score:
            return "dealer"
        else:
            return "draw"
    else:
        return "next"

def blackjackgame(rounds, is_pass1):

    add_cards(rounds=rounds, is_pass=is_pass1)
    customer_score = score_calc(customer_cards)
    dealer_score = score_calc(dealer_cards)

    status = score_check(customer_score, dealer_score, is_pass1)
    print("------------------------------------------------------------------")
    if not is_pass1:
        print(f"Dealer's First Card is {dealer_cards[0]}")
    print(f"Your Cards {customer_cards}, current score {customer_score}")

    if status == 'customer':
        print(f"Dealer's Cards {dealer_cards} , dealer's score {dealer_score}")
        print("Congratulation... You Won")
    elif status == 'dealer':
        print(f"Dealer's Cards {dealer_cards}, dealer's score {dealer_score}")
        print("Ohh Snap... Dealer Won")
    elif status == 'draw':
        print(f"Dealer's Cards {dealer_cards}, dealer's score {dealer_score}")
        print("Match is Draw")
    elif status == 'next':
        isnext = (input('Type \'y\' to get another card, type \'n\' to pass: ')).lower()
        if isnext == 'n':
            is_pass1 = True
        rounds = rounds + 1
        blackjackgame(rounds, is_pass1)
    else:
        print(f"Dealer {dealer_cards}, score {dealer_score}")
        print(f"Customer {customer_cards}, score {customer_score}")
        print(f"is Pass {is_pass1}")
        print("Sorry.... Some Unexpected Scenario Occurred. Try again")



gameChoice = (input("Do you want to play the Black Jack game...?\n1. yes\n2. no\n")).lower()
if gameChoice == 'yes' or gameChoice == '1':
    is_pass = False
    blackjackgame(rounds= 1, is_pass1= is_pass)
else:
    print("Thank you have a nice day")



