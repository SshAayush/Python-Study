from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os

clear = lambda: os.system('cls')
clear()

should_stop = False
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
 
while not should_stop:
    u_choice = input("What would you like? (espresso/latte/cappucciono): ").lower()
    if u_choice == 'off':
        should_stop = True
        break
    elif u_choice == 'report':
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(u_choice)
        
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
