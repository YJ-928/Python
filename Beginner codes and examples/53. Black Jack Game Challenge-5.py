import random
# 11 is the Ace.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Hint 4


def deal_card():
    """Returns a random card from the deck of cards"""
    card = random.choice(cards)
    return card

# Hint 6, 7 and 8


def calculate_score(List):
    """takes a List of cards as input and 
    returns the sum of them as score."""
    # Black Jack check
    if len(List) == 2 and sum(List) == 21:
        return 0
    # Ace check for over 21 score
    if sum(List) > 21 and 11 in List:
        List.remove(11)
        List.append(1)
    return sum(List)

# TODO:- Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.


def compare(user_res, computer_res):
    if user_res == computer_res:
        return print("Its a draw")
    elif user_res == 0:
        return print("User Wins")
    elif computer_res == 0:
        return print("Computer Wins")
    elif user_res > 21:
        return print("Computer Wins")
    elif computer_res > 21:
        return print("Player Wins")
    elif user_res > computer_res:
        return print("Player Wins")
    else:
        return print("Computer Wins")


# Hint 5
user_cards = []
computer_cards = []

for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

# Hint 11:
while True:

    user_res = calculate_score(user_cards)
    computer_res = calculate_score(computer_cards)
    print(f"Your Cards: {user_cards}, current score: {user_res}")
    print(f"Computer's First card: {computer_cards[0]}")

    # # Hint 9
    # if user_res == 0 or computer_res == 0:
    #     print("BlackJack, Game Ends here")
    #     print(f"Your Cards: {user_cards}, current score: {user_res}")
    #     print(
    #         f"Computer's cards: {computer_cards}, computer score: {computer_res}")
    #     break

    # elif user_res > 21:
    #     print("Computer Wins, Player score Exceeds 21")
    #     print(f"Your Cards: {user_cards}, current score: {user_res}")
    #     print(
    #         f"Computer's cards: {computer_cards}, computer score: {computer_res}")
    #     break

    # Hint 10:
    draw_again = input(
        "Do you want to draw another card? type 'y' for yes 'n' for no ")
    if draw_again.lower() == 'y':
        user_cards.append(deal_card())
    else:
        break

# Hint 12
while computer_res != 0 and computer_res < 17:
    computer_cards.append(deal_card())
    computer_res = calculate_score(computer_cards)


# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
