import random
from art import logo
from art import vs
from game_data import data
import os

clear = lambda: os.system('cls')
score = 0
print(logo)

def choose():
        given_dictonary = random.choice(data)
        return given_dictonary


def play(u_score):
    global score
    a_op = int(cache_a['follower_count'])
    b_op = int(given_option['follower_count'])
    print(a_op)
    print(b_op)
    
    if u_choice == 'a' and a_op > b_op:
        clear()
        print(logo)
        score += 1
        print(f"You're right! Current score: {score}")
    elif u_choice == 'b' and b_op > a_op:
        clear()
        print(logo)
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        clear()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        return True


cache_a = choose()
should_stop = False

while not should_stop == True:
    print(f"Compare A: {cache_a['name']}, a {cache_a['description']}, from {cache_a['country']}")
    print(cache_a['follower_count'])
    print(vs)
    given_option = choose()
    print(f"Against B: {given_option['name']}, a {given_option['description']}, from {given_option['country']}")
    print(given_option['follower_count'])
    u_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    should_stop = play(u_choice)
    cache_b = given_option
    cache_a = cache_b