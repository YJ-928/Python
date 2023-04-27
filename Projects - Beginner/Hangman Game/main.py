# The Hangman Game
# importing path from os to import req python files as modules & importing other req lib's
from os import path
from words import word_list
from art import logo, stages
import random
import time

# loop for resetting the game
while True:
    # setting up the random word gen to get this game started
    chosen_word = random.choice(word_list)

    # creating the number of blanks equal to our chosen_word
    display = []
    for letters in chosen_word:
        display += "_"

    # creating variable to keep count of player's lives
    lives = 6
    Victory = False

    # Lets start the game
    print("\n\nWelcome to the Hangman game created by YJ-928\n", logo, "\n")
    time.sleep(1)

    # starting the game in dramatic way:
    i = 3
    print("Are you ready?\n")
    while i != 0:
        print(f"The Game Starts in {i} seconds..")
        i -= 1
        time.sleep(1)

    # to print total number of letter's as blanks to help the player guess
    print(
        f"\nYour word has {len(chosen_word)} number of blanks, Good Luck!!\n")
    time.sleep(1)

    # While loop until the player guesses the word right or runs out of lives
    while not Victory:

        # asking the user for their letter guess
        print('\n', display)
        guess = input("\nGuess a letter: ").lower()

        if guess in display:
            print(f"You've already guessed {guess}")

        # replacing the blank in display with correctly guessed letter's
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = guess

        if guess not in chosen_word:
            print(
                f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1
            # if player runs out of lives GameOver
            if lives == 0:
                print("\nYou Lost :( ")
                print(f"The word you were guessing was {chosen_word}")
                break

        print(stages[lives])

        if "_" not in display:
            print("\nYou Win :) , you guessed all the letter's right! ")
            # Join all the elements in the list and turn it into a String and display result
            print(f"\n{' '.join(display)}")
            Victory = True

    if input("Do you wish to play again? type Y or N: ").upper() == "N":
        break
