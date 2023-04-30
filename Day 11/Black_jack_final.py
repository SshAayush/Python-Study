import random
import os
from art import logo

clear = lambda: os.system('cls')
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

user_cards = deal_card()
computer_cards = deal_card()

def user_score(user_cards):
    sum = 0
    for card in user_cards:
        sum += card  
    return sum
def computer_score(computer_cards):
    sum = 0
    for card in computer_cards:
        sum += card
    return sum

def final_result(u_sum,c_sum):
    if u_sum > 21:
        print("Bust!! You went over")
    elif c_sum > 21:
        print("You won!")
    elif u_sum == 21 or c_sum == 21:
        print("Black Jack!! You win")
    elif u_sum == c_sum:
        print("Draw")
    elif u_sum > c_sum:
        print("You win!")
    elif u_sum < c_sum:
        print("You lose!")
        
def play_game(sum):
    print(logo)
    user_cards = []
    computer_cards = []
    game_over = False
    
    for _ in range(0,2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not game_over:
        u_sum = user_score(user_cards)
        c_sum = computer_score(computer_cards)
        if user_cards == 11 and u_sum < 21:
            user_cards.remove(11)
            user_cards.append(1)

        if computer_cards == 11 and c_sum < 21:
            computer_cards.remove(11)
            computer_cards.append(1)
        print(f"Your cards: {user_cards}, current score :{u_sum}")
        print(f"Computer's first card: {computer_cards[0]}")
        while c_sum != 0 and c_sum < 17:
            computer_cards.append(deal_card())
            c_sum = computer_score(computer_cards)
        if u_sum > 21:
            final_result(u_sum,c_sum)
            game_over = True
            break
        elif u_sum == 21 or c_sum == 21:
            final_result(u_sum,c_sum)
            break
        add_hand = input("Type 'y' to get another card, type 'n' to pass: ")
        
        if add_hand == 'n':
            print(f"Your final hand: {user_cards}, final_score: {u_sum}")
            print(f"Computer's final hand: {computer_cards}, final score: {c_sum}") 
            final_result(u_sum,c_sum)
            game_over = True
        elif add_hand == 'y':
            user_cards.append(deal_card())
            print(f"Your cards: {user_cards}, current score: {u_sum}")
            print(f"Computer first card: {computer_cards[0]}")
            if u_sum > 21:
                final_result(u_sum,c_sum)
            

# start_game = False
# while not start_game:
#     start_game = input("Do you want to play game of BlackJack? type 'y' or  'n'")
while input("Do you want to start the game? Type 'y' or 'n':") == "y":
    clear()
    play_game(sum)