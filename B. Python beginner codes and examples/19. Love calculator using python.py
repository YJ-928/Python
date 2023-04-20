# Love calculator using python
# Determines Love Score on occurrances of words "TRUE" & "LOVE"
# in your and their names, then based on same output is printed

yourName = input("Welcome to the Love Calculator!!\nEnter your name  ")
theirName = input("Enter their name  ")

# calculating LoveScore based on counts of TRUE, LOVE in names.
LoveScore = int(str(yourName.upper().count("T") + yourName.upper().count("R") +
                    yourName.upper().count("U") + yourName.upper().count("E") +
                    theirName.upper().count("T") + theirName.upper().count("R") +
                    theirName.upper().count("U") + theirName.upper().count("E")) + str(theirName.upper().count("L") + theirName.upper().count("O") +
                                                                                       theirName.upper().count("V") + theirName.upper().count("E") +
                                                                                       yourName.upper().count("L") + yourName.upper().count("O") +
                                                                                       yourName.upper().count("V") + yourName.upper().count("E")))

# printing personalized results based on value of LoveScore
print(f"\nYour Love Score is {LoveScore}, {yourName} Loves {theirName} as coke loves mentos!!\n") if (LoveScore >= 90 or LoveScore <= 10) else print(
    f"\nYour Love Score is {LoveScore}, {yourName} and {theirName} are alright together\n") if (LoveScore >= 40 and LoveScore < 50) else print(f"\nYour Love Score is {LoveScore}\n")
