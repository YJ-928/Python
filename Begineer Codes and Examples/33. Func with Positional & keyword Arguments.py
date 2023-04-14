# Function with more than One input
def greet_ppl(name, location):
    print(f"Hello {name}!,\nWhat is it like in {location}?")


# calling the function
greet_ppl(input("Enter your name: "), input("Enter your location: "))


def greet_ppl_keyword(name, location):
    # function with keyword argument
    print(f"Hello {name}!,\nWhat is it like in {location}?")


# calling function with keyword arguments
greet_ppl_keyword(name=input('Enter your name: '),
                  location=input("Enter your location: "))
