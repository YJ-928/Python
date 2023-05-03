import os
from os import path
from art import logo
from time import sleep

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def fetch_ingredients_and_make_coffee(coffee_type):
    """Takes Coffee type and Fetches the required Ingredients 
    and Makes our Coffee.(ie, Subtracts Ingredients from resources)."""
    global resources
    # fetching the extact ingredients based on the coffee type
    if coffee_type == "espresso":
        coffee_Ingre = MENU["espresso"]["ingredients"]

    elif coffee_type == "latte":
        coffee_Ingre = MENU["latte"]["ingredients"]

    elif coffee_type == "cappuccino":
        coffee_Ingre = MENU["cappuccino"]["ingredients"]

    # subtracting the ingredients from resources only if they are > 0
    if resources["water"] > 0:
        resources["water"] -= coffee_Ingre["water"]
    else:
        print("Sorry there is not enough water. Money Refunded.")
        sleep(1)
        exit()

    if resources["milk"] > 0:
        resources["milk"] -= coffee_Ingre["milk"]
    else:
        print("Sorry there is not enough milk. Money Refunded.")
        sleep(1)
        exit()

    if resources["coffee"] > 0:
        resources["coffee"] -= coffee_Ingre["coffee"]
    else:
        print("Sorry there is not enough coffee. Money Refunded.")
        sleep(1)
        exit()

    return resources


def process_coins():
    """Returns the total calculated from the coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def coffee_machine():
    while True:
        print(logo)
        user_choice = input(
            "What would you like? (espresso/latte/cappuccino): ").lower()
        # clear,off,report and reset are secert commands only for the coffee machine owner.
        if user_choice == "clear":
            os.system('cls')
            coffee_machine()
        if user_choice == "off":
            print("Command Accepted, Switching OFF now")
            sleep(2)
            os.system('cls')
            exit()
        if user_choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${profit}")
        if user_choice == "reset":
            print("Command Accepted, Resources are been refilled.. please wait")
            i = 3
            while i != 0:
                sleep(1)
                print(f"Done in {i}...")
                i -= 1
            print("Done, Resources are refilled.")
            sleep(1)
            coffee_machine()
        elif user_choice in ["espresso", "latte", "cappuccino"]:
            coffee_cost = MENU[user_choice]["cost"]
            print(
                f"You have selected {user_choice}, Total cost is ${coffee_cost}")
            money = process_coins()
            if is_transaction_successful(money, coffee_cost):
                fetch_ingredients_and_make_coffee(user_choice)
                print(f"Here is your {user_choice} ☕️. Enjoy!")


coffee_machine()
