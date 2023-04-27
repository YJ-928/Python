from time import sleep
# Calculator


def Add(a, b):
    """Addition Function
    returns a + b """
    result = a + b
    return result


def Sub(a, b):
    """Subtract Function
    returns a - b """
    result = a - b
    return result


def Mul(a, b):
    """Multiplication Function
    returns a * b """
    result = a * b
    return result


def Div(a, b):
    """Division Function
    returns a / b """
    result = a / b
    return result


operations = {
    "+": Add,
    "-": Sub,
    "*": Mul,
    "/": Div,
}


def Calculator():
    # looping condition declaration
    Done = False

    num1 = float(input("What is the first number? "))
    for symbols in operations:
        print(symbols)
    operation_symbol = input("Pick an operation symbol from above line ")
    num2 = float(input("Enter the second number: "))

    while not Done:
        calulation = operations[operation_symbol]
        result = calulation(num1, num2)
        print(f"\n{num1} {operation_symbol} {num2} = {result}\n")
        Continue = input(
            "Do you wish to continue the calculations, type 'y' for yes or 'n' for no  ")
        if Continue.lower() == 'y':
            num1 = result
            num2 = int(input("Whats the next number? "))
            for symbols in operations:
                print(symbols)
            operation_symbol = input(
                "Pick an operation symbol from above line ")

        elif Continue.lower() == 'n':
            Done = True
            Calculator()
