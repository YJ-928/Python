# FizzBuzz Challenge
for number in range(int(input("\n\nWelcome to FizzBuzz Py-Challenge\nEnter the Starting number: ")), int(input("Enter the Ending or last number: ")) + 1):
    print("FizzBuzz") if number % 3 == 0 and number % 5 == 0 else print(
        "Fizz") if number % 3 == 0 else print("Buzz") if number % 5 == 0 else print(number)
