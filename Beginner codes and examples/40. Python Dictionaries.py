# Declaring a dictionary in python
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Retriving the value from a dictionary
print(programming_dictionary["Bug"])
print(programming_dictionary["Function"])

# Changing the value of a key in dictionary
programming_dictionary["Bug"] = "An Error in your program is called a Bug"

# printing out whole dictionary
print(programming_dictionary)

# printing each key and value seperately
for key in programming_dictionary:
    print("The Key is:-", key)
    print("Its Value is:-", programming_dictionary[key])
