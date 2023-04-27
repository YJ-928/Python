# The Caeser Cipher
# encode or decode your text using your own secret key (shift_amount)

# importing required libraries
from os import path
from art import logo
import time

# creating a alphabet array to shift letters from and to new positions inside user_text
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# while loop condition
Quit = False


def CaesarCipher(plain_text, shift_amount, cipher_direction):
    """ a function to do encoding and decoding """
    end_chipher = ""  # empty string
    end_text = "encoded"
    # making shift_amount negative if direction is decode
    if cipher_direction == 'decode':
        shift_amount *= -1
        end_text = "decoded"
    # main loop
    for letter in plain_text:
        if letter not in alphabet:
            # if a number, symbol or a space leave it as it is
            end_chipher += letter
        else:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            end_chipher += alphabet[new_position]

    return print(f"\nThe {end_text} text is:\n{end_chipher}\n")


while not Quit:
    # welcome msg and logo
    print("\n\nWelcome to Caeser Cipher created by YJ-928\n", logo)

    # taking inputs
    direction = input(
        "\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("\nType your message:\n").lower()
    shift = int(input("\nType the shift number:\n"))

    # if the user enters a shift number greater than 26.
    shift = shift % 26

    # calling function
    CaesarCipher(plain_text=text, shift_amount=shift,
                 cipher_direction=direction)

    # end loop condition, if user wants to quit
    if input("\ndo you want to encode/decode again? type Y or N: ").upper() == "N":
        Quit = True
