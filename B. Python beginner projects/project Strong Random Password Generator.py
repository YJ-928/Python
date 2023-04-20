# Password Generator Project
import random
import time
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("\nWelcome to the PyPassword Generator by YJ-928")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# creating an empty list
Password_List = []

# looping and appending user specified random characters to the Password_List
for letter in range(0, nr_letters+1):
    Password_List.append(random.choice(letters))

for symbol in range(0, nr_symbols+1):
    Password_List.append(random.choice(symbols))

for number in range(0, nr_numbers+1):
    Password_List.append(random.choice(numbers))

# Shuffling the contents of Password_List to mix above 3 categories
random.shuffle(Password_List)

# initializing an empty string
password = " "

# Converting the Password_List to string
for item in Password_List:
    password += str(item)

# printing out the strong user specific created password
print(f"\nYour Password is:  {password}\n\n")
time.sleep(5)
