# calculates the total bill including tip that each person needs to pay

print("\n\nWelcome to the tip calculator")
bill = float(input("What was the total bill?  $"))
tip_percent = int(
    input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# calculating tip using tip percent giving by user: tip = tip_percent/100 * bill
# bill per person = bill + tip / people & rounding it to 2 decimals.
amount_to_pay = round((bill + ((tip_percent / 100) * bill)) / people, 2)

# to get output as $20.60 instead of $20.6, we use .format function.
# Syntax: ":.Number of decimal_places".format(variable_containing_value)

print("Each person should pay: ${0:.2f}\n\n".format(amount_to_pay))
