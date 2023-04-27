from os import path
from art import logo
import time

while True:
    # Welcome Drawing
    print(logo)

    time.sleep(2)
    # Welcome Message
    print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

    time.sleep(2)
    # Choice-1 Game starts
    choice1 = input(
        'You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()

    time.sleep(2)
    # Choice-2 and Choice-1 Consequences
    choice2 = input(
        'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower() if choice1 == "left" else print("You fell into a hole. Game Over.")

    time.sleep(2)
    # Choice-3 and Choice-2 Consequences
    choice3 = input(
        "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower() if choice2 == "wait" else print("You get attacked by an angry trout. Game Over.")

    time.sleep(2)
    # Choice-3 Consequences
    print("It's a room full of fire. Game Over.") if choice3 == "red" else print(
        "You found the treasure! You Win!") if choice3 == "yellow" else print("You enter a room of beasts. Game Over.") if choice3 == "blue" else print("You chose a door that doesn't exist. Game Over.")

    playAgain = input("Do you want to play again? Y or N  ")
    if playAgain.upper() == "N":
        break
