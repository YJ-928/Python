def checkPrime(Number):
    for i in range(2, Number):
        return print(f"{Number} is not a prime number.") if Number % i == 0 else print(f"{Number} is a prime number.")


checkPrime(Number=int(input("\nEnter a number: ")))
