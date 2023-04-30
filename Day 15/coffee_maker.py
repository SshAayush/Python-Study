import os

clear = lambda: os.system('cls')
clear()
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


money = int(0)

should_stop = False
emote = "☕"

def extract_qty(u_choice):
    r_water = (MENU[u_choice]['ingredients']['water'])
    if u_choice == 'latte' or u_choice == 'cappuccino':
        r_milk = (MENU[u_choice]['ingredients']['milk'])
    else:
        r_milk = 0
    r_coffee = (MENU[u_choice]['ingredients']['coffee'])
    return r_water,r_milk,r_coffee

def check_qty():
    if resources['water'] >= u_drink[0]:
        if resources['milk'] >= u_drink[1]:
            if resources['coffee'] >= u_drink[2]:
                resources['water'] -= u_drink[0]
                resources['milk'] -= u_drink[1]
                resources['coffee'] -= u_drink[2]
                return False
            else:
                print("Sorry there is not enough coffee.")
                return True
        else:
            print("Sorry there is not enough milk.")
            return True
    else:
        print("Sorry there is not enough water.")
        return True
 
coins = {
    "quarter" : 0.25,
    "dime" : 0.10,
    "nickel" : 0.05,
    "penny" : 0.01, 
},
    
def check_coin(u_choice):
    drink_cost = (MENU[u_choice]['cost'])
    print("Please insert coins.")
    quarters = (int(input("How many quarters?: $")))*0.25
    dimes = (int(input("How many dimes?: $")))*0.10
    nickles = (int(input("How many nickles?: $")))*0.05
    pennies = (int(input("How many pennies?: $")))*0.01
    total = quarters + dimes + nickles + pennies
    if total >= drink_cost:
        return_cur = format(total - drink_cost,".2f")
        print(f"Here is ${(return_cur)} in change.")
        print(f"Here is your {u_choice} {emote}. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded")
    
# TODO: 1. Print report of resources.
while not should_stop:
    u_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if u_choice == 'report':
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    elif u_choice == 'espresso' or 'latte' or 'cappuccino':
        u_drink = []
        u_drink = extract_qty(u_choice)
        should_stop = check_qty()
        if should_stop == False:
            check_coin(u_choice)

