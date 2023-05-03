import random
# 11 is the Ace.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Hint 4


def deal_card():
    """Returns a random card from the deck of cards"""
    card = random.choice(cards)
    return card

# TODO:-
# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.
# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().


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

print(user_cards, user_res)
print(computer_cards, computer_res)
