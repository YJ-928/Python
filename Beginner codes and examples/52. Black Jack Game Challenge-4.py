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


# Hint 5
user_cards = []
computer_cards = []

for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

# TODO:-
# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
while True:

    user_res = calculate_score(user_cards)
    computer_res = calculate_score(computer_cards)
    print(f"Your Cards: {user_cards}, current score: {user_res}")
    print(f"Computer's First card: {computer_cards[0]}")

    # Hint 9
    if user_res == 0 or computer_res == 0:
        print("BlackJack, Game Ends here")
        print(f"Your Cards: {user_cards}, current score: {user_res}")
        print(
            f"Computer's cards: {computer_cards}, computer score: {computer_res}")
        break

    elif user_res > 21:
        print("Computer Wins, Player score Exceeds 21")
        print(f"Your Cards: {user_cards}, current score: {user_res}")
        print(
            f"Computer's cards: {computer_cards}, computer score: {computer_res}")
        break

    # TODO:-
    # Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
    draw_again = input(
        "Do you want to draw another card? type 'y' for yes 'n' for no ")
    if draw_again.lower() == 'y':
        user_cards.append(deal_card())
    else:
        break

# TODO:-
# Hint 12: Once the user is done, it's time to let the computer play.
# The computer should keep drawing cards as long as it has a score less than 17.
while computer_res != 0 and computer_res < 17:
    computer_cards.append(deal_card())
    computer_res = calculate_score(computer_cards)
