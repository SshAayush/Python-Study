
import random
from art import logo
import os

clear = lambda: os.system('cls')
easy_lives = 10
hard_lives = 5
print(logo)
actual_number = random.randint(1,100)

def lives():
    global easy_lives, hard_lives
    if difficulty == 'easy':
        return easy_lives
    elif difficulty == 'hard':
        return hard_lives
    else:
        print("typo?? Check your input")

def calculation(choice,f_lives):
    global actual_number
    if choice > actual_number:
        print("Too high.")
        return f_lives - 1
    elif choice < actual_number:
        print("Too low.")
        return f_lives - 1
    else:
        print(f"You got it! The answer was {actual_number}")
        return f_lives == 0

print(f"Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nThe correct answer is {actual_number} ")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
f_lives = lives()
count_lives = f_lives
while f_lives != 0:
    print(f"You have {f_lives} attempts remaning to guess number.")
    choice = int(input("Make a guess: "))
    f_lives = calculation(choice,f_lives)
    count_lives -= 1
    if count_lives == 0:
        print("You've run out of guesses, you lose.")