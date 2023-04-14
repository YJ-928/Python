import random

# taking input as string & converting it to a list using split function
names = input("Give me everybody's names,separated by a comma. ").split(", ")

print(f"{random.choice(names)} is going to buy the meal today!")
