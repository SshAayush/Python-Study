import random
import sys

rock = ''''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper = '''
     _______
---'    ____)____
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

game = [rock,paper,scissors]
you_chose = int(input("Enter your choice 0-Rock, 1-Paper, 2-Scissors:"))
if(you_chose>2 or you_chose<0):
    print("You typed an invalid number!!")
    sys.exit()
print(f"Your Choice:\n{game[you_chose]}\n")
comp_chose = random.randint(0,2)
print(f"\nComputer Chose {game[comp_chose]}")

if(you_chose == 0 and comp_chose == 2 ):
    print("You Won!!")
elif(you_chose == 0 and comp_chose == 1):
    print("You lose!!")

if(you_chose == 1 and comp_chose == 0 ):
    print("You Won!!")
elif(you_chose == 1 and comp_chose == 2):
    print("You lose!!")

if(you_chose == 2 and comp_chose == 1 ):
    print("You Won!!")
elif(you_chose == 2 and comp_chose == 0):
    print("You lose!!")
elif(you_chose == comp_chose):
    print("Draw!!")