# calculates life left with us until we are 90 years old
# 365 Days, 52 Weeks and 12 Months considering this

user_age = int(input('How old are you ? [Enter age in years]:\t'))

print(
    f"\nYou have {365*(90 - user_age)} days, {52*(90 - user_age)} weeks and {12*(90 - user_age)} months left.\n")
