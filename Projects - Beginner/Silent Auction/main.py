# importing lib's
import os
from time import sleep
from os import path
from art import logo


def find_highest_bidder(Auction):
    Highest_Bid = 0
    Highest_Bidder = ""
    for Bidder in Auction.keys():
        Bid_amount = Auction[Bidder]
        if Bid_amount > Highest_Bid:
            Highest_Bid = Bid_amount
            Highest_Bidder = Bidder
    return print(f"\nThe Winner of this auction is {Highest_Bidder} with ${Highest_Bid} Bid\nThe item is sold to {Highest_Bidder}\n\n")


# empty dictionary
Auction = {}

# printing the Ascii art
print("\n\nWelcome to the Silent Auction by YJ-928\n", logo)

# Declaring the while loop end condition:
Quit = False

# loop to get all Biders Bids
while not Quit:
    # taking input's and simultaneously calling the function
    Name = input('What is your name? ')
    Value = int(input('How much do you want to bid? $ '))
    Auction[Name] = Value
    # checking for other bidders
    End = input("Are there any other bidders? Type 'yes' or 'no'  ")
    if End.upper() == "NO":
        Quit = True
        print(Auction)
        # Calling our function
        find_highest_bidder(Auction)
    else:
        os.system('cls')


sleep(5)
