# import lib
import random
import time

# ASCII arts
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
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

welcome = '''
Rock             Paper                 Scissor
    _______          _______               _______             
---'   ____)     ---'   ____)____      ---'   ____)____                   
      (_____)              ______)               ______)                     
      (_____)              _______)           __________)                      
      (____)              _______)           (____)                    
---.__(___)      ---.__________)       ---.__(___)                                                                                                                                       

'''
while True:
    # Welcome message and game start
    print(
        f"\n\nWelcome to ROCK PAPER & SCISSORS GAME BY YJ-928\n{welcome}")
    time.sleep(2)

    # taking user input
    User_Choice = input(
        "What Do You Choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n")
    time.sleep(1)

    # printing user input equivalent ASCII Art
    print("\nYou Chose\n")
    print(rock) if User_Choice == "0" else print(
        paper) if User_Choice == "1" else print(scissors)

    # computer choice generation
    Computer_Choice = str(random.randrange(0, 3))
    time.sleep(1)

    # printing Computer choice equivalent ASCII Art
    print("\nComputer Chose\n")
    print(rock) if Computer_Choice == "0" else print(
        paper) if Computer_Choice == "1" else print(scissors)

    # printing final win,lose or tie result
    print("\n👑 You Win 👑\n") if User_Choice == 0 and Computer_Choice == 2 else print("\n🥹 🥺 You Lose 🥹 🥺\n") if User_Choice == 2 and Computer_Choice == 0 else print(
        "\n👑 You Win 👑\n") if User_Choice > Computer_Choice else print("\n🥹 🥺 You Lose 🥹 🥺\n") if User_Choice < Computer_Choice else print("\n🤝 Its a Tie 🤝\n")

    if input("Do you want to play again? Y or N ").upper() == "N":
        break
