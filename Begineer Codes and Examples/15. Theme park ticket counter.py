# Theme park ticket counter senario program
age = int(input("Welcome to the Theme park\nPlease enter your age in years "))
print("Your ticket is $12") if age >= 18 else print("Your ticket is $7") if (
    age < 18 and age >= 12) else print("Your ticket is $5")
