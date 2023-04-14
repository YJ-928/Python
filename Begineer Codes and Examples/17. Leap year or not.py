# Leap year finder/checker:-
Year = int(input("Enter the year to check "))

# A year is a Leap year if completely divisible by 4,100 and 400.. Or
# A year is also a Leap year if completely divisible by 4 and 400 but not divisible by 100.

print(f"{Year} is a Leap year") if ((Year % 4 == 0) and (Year % 100 == 0) and (Year % 400 == 0)) else print(
    f"{Year} is a Leap year") if ((Year % 4 == 0) and (Year % 100 != 0)) else print(f"{Year} is not a Leap year") if ((Year % 4 == 0) and (Year % 100 == 0) and (Year % 400 != 0)) else print(f"{Year} is not a Leap year")
