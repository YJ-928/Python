# Traditional Cal function
# def Calculator(num1, num2, symbol):
#     if symbol == "+":
#         return Add(num1, num2)
#     if symbol == "-":
#         return Sub(num1, num2)
#     if symbol == "*":
#         return Mul(num1, num2)
#     if symbol == "/":
#         return Div(num1, num2)
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

num1 = int(input("What is the first number? "))

for symbols in operations:
    print(symbols)

operation_symbol = input("Pick an operation symbol from above line ")

num2 = int(input("Enter the second number: "))

# fetching the function based on user input
Calculation_function = operations[operation_symbol]
# Providing the choosen function with inputs
# storing the output in "result"
first_result = Calculation_function(num1, num2)
# printing the output
print(f"{num1} {operation_symbol} {num2} = {first_result}")

# continuing the operation on previous results
for symbols in operations:
    print(symbols)
operation_symbol = input("Pick an operation symbol from above line ")
num3 = int(input("What's The Next Number: "))

# fetching the function based on user input
Calculation_function = operations[operation_symbol]
# storing the output in "result"
second_result = Calculation_function(num1, num2)
# printing the output
print(f"{first_result} {operation_symbol} {num3} = {second_result}")
