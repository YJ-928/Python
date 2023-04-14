print("\nWelcome to Even/Odd Sum PyCalculator\n")

total = 0
First_Value = int(input("\nEnter the First Value: "))
Last_Value = int(input("\nEnter the Last Value: "))
Even_or_Odd = int(input("\nEnter 1 for Odd-Sum or 2 for Even-Sum: "))

for items in range(First_Value, Last_Value+1, Even_or_Odd):
    total += items

print(
    f"\nTotal Sum of Number's between {First_Value} and {Last_Value} is: {total}\n")
