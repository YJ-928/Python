# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# fetch the invited names as a list
with open("Input/Names/invited_names.txt", "r") as file:
    invited_names = file.readlines()

# fetching the starting letter as a list
with open("Input/Letters/starting_letter.txt", "r") as file:
    starting_letter = file.readlines()

# loop to replace all the dear [name] with actual names
# used a for loop to get rid of the '\n' char
# wrote each letter to a seperate file
# creating a mail for each of the names in invited_names
count = 0
while count < len(invited_names):
    name = ""
    name_raw = invited_names[count]
    for i in name_raw:
        if i == '\n':
            continue
        name += i
    starting_letter[0] = f"Dear {name}\n"
    with open(f"Output/ReadyToSend/Letter_to_{name}.txt", "w") as file:
        file.writelines(starting_letter)

    count += 1
