import random

choice = input(
    "\nWelcome to the Virtual Coin Toss Generator\nWhat would you like to choose Heads or Tails ?  ")

if random.randrange(0, 2) == 1 and choice == "Heads":
    print("\nCoin Shows Heads, You Win!!\n")
elif random.randrange(0, 2) == 1 and choice == "Tails":
    print("\nCoin Shows Heads, You Lose\n")
elif random.randrange(0, 2) == 0 and choice == "Heads":
    print("\nCoin Shows Tails, You Lose\n")
elif random.randrange(0, 2) == 0 and choice == "Tails":
    print("\nCoin Shows Tails, You Win!!\n")
