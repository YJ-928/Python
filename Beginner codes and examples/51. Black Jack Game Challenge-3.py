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

user_res = calculate_score(user_cards)
computer_res = calculate_score(computer_cards)

# print(user_cards, user_res)
# print(computer_cards, computer_res)

print(f"Your Cards: {user_cards}, current score: {user_res}")
print(f"Computer's First card: {computer_cards[0]}")

# TODO:- Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

if user_res == 0 or computer_res == 0:
    print("BlackJack, Game Ends here")
    print(f"Your Cards: {user_cards}, current score: {user_res}")
    print(
        f"Computer's cards: {computer_cards}, computer score: {computer_res}")

elif user_res > 21:
    print("Computer Wins, Player score Exceeds 21")
    print(f"Your Cards: {user_cards}, current score: {user_res}")
    print(
        f"Computer's cards: {computer_cards}, computer score: {computer_res}")
