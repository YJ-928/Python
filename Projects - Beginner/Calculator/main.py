import os
from os import path
from art import logo
from time import sleep


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


def calculator():
    print(logo)
    sleep(1)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    Done = False

    while not Done:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            sleep(1)
            Done = True
            os.system('cls')
            calculator()


calculator()
