# Defining the functions
def Greet():
    # simple function
    print(f"Hello {input('Enter your name: ')}\nWelcome to PyGreet function")


def Greet_with(name):
    # function with inputs
    print(f"Hello {name}\nHow are you doing {name}?")


# Calling the functions (Executing them)
Greet()
Greet_with("Yash")
