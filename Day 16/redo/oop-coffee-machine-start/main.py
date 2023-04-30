from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os

clear = lambda: os.system('cls')
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
should_stop = False
clear()
while not should_stop:
    u_choice = input("What would you like? test (espresso/latte/cappucino): ").lower()
    if u_choice == 'off':
        should_stop = True
        clear()
        break
    elif u_choice == 'report':
        drink_report = coffee_maker.report()
        money_report = money_machine.report()
    else:
        drink = menu.find_drink(u_choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)