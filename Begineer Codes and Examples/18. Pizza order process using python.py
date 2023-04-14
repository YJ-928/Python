# pizza order process using python
# S, M, L : $15, $20, $25 respectively
# pepperoni for S, M, L : +$2, +$3, +$4 resp.
# extra cheese : +$1

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L?  ")
pepperoni = input("Do you want pepperoni? Y or N  ")
cheese = input("Do you want extra cheese? Y or N  ")

# Calculating, Checking condition and printing
print(f"\nYour final bill is $18\n") if (size.upper() == "S" and pepperoni.upper() == "Y" and cheese.upper() == "Y") else print(f"\nYour final bill is $17\n") if (size.upper() == "S" and pepperoni.upper() == "Y" and cheese.upper() == "N") else print(f"\nYour final bill is $15\n") if (size.upper() == "S" and pepperoni.upper() == "N" and cheese.upper() == "N") else print(f"\nYour final bill is $24\n") if (size.upper() == "M" and pepperoni.upper() == "Y" and cheese.upper() == "Y") else print(
    f"\nYour final bill is $23\n") if (size.upper() == "M" and pepperoni.upper() == "Y" and cheese.upper() == "N") else print(f"\nYour final bill is $20\n") if (size.upper() == "M" and pepperoni.upper() == "N" and cheese.upper() == "N") else print(f"\nYour final bill is $31\n") if (size.upper() == "L" and pepperoni.upper() == "Y" and cheese.upper() == "Y") else print(f"\nYour final bill is $30\n") if (size.upper() == "L" and pepperoni.upper() == "Y" and cheese.upper() == "N") else print(f"\nYour final bill is $21\n") if (size.upper() == "L" and pepperoni.upper() == "N" and cheese.upper() == "Y") else print(f"\nYour final bill is $21\n") if (size.upper() == "M" and pepperoni.upper() == "N" and cheese.upper() == "Y") else print(f"\nYour final bill is $16\n")
