import random
import os
from turtle import goto
from art import logo

clear = lambda: os.system('cls')

def user_card_gen ():
    user_cards.append(random.choice(cards))
    return user_cards
    
def computer_card_gen ():
    computer_cards.append(random.choice(cards))
    return computer_cards

def calculate_card (user_card, computer_card):

    print(f"Your cards: {user_card}, current score: {sum(user_card)}")
    print(f"Computer's first card: {computer_card[0]}")
    game_re = input("Type 'y' to get another card, type 'n' to pass:")
    while game_re == "y":
        user_card = user_card_gen()
        computer_card = computer_card_gen ()
        if sum(user_card) > 21:
            game_re = "n"
        calculate_card(user_card, computer_card)
    if game_re == "n":
        print(f"Your final hand: {user_card}, final score: {sum(user_card)}")
        print(f"Computer's final: {computer_card}, final score {sum(computer_card)}")
        if sum(user_card) > 21:
            print("You went over. You lose ☠")
        elif sum(user_card) > sum(computer_card):
            print("You win 🤩")
        else:
            print("You lose ☠")



cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
should_start = True


while should_start:
    
    game_start = input ("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if game_start == "y":
        should_start = True
        clear()
        computer_cards = []
        user_cards = []
        user_cards.append(random.choice(cards))
        print(logo)
        user_card = user_card_gen()
        computer_card = computer_card_gen ()
        calculate_card(user_card, computer_card)

    else:
        should_start = False