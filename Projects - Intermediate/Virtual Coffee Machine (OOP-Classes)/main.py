# importing modules
import os
from time import sleep
from os import path
# importing self-created modules
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo

# assigning objects
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def coffeeMachine():
    while True:
        print(logo)
        user_choice = input(
            f"\nWhat would you like? ({menu.get_items()}): ").lower()
        if user_choice == "off":
            break
        elif user_choice == "report":
            coffee_maker.report()
            money_machine.report()
        elif user_choice in ["latte", "espresso", "cappuccino"]:
            order = menu.find_drink(user_choice)
            print(
                f"\nOrder Details:-\nName: {order.name}\nCost: ${order.cost}")
            if money_machine.make_payment(order.cost) == True:
                if coffee_maker.is_resource_sufficient(order) == True:
                    coffee_maker.make_coffee(order)


coffeeMachine()
