import random
# TODO:-
# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    """Returns a random card from the deck of cards"""
    card = random.choice(cards)
    return card


# TODO:-
# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
user_cards = []
computer_cards = []

for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

print(user_cards, computer_cards)
