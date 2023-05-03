from prettytable import PrettyTable

# setting an object to class
table = PrettyTable()

# creating a Pokemon table using above object
# add_column("Fieldnames/Heading",[ordered list for the data below])
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmandar"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# changing our table styles
# left alignment
table.align = "l"

# printing the created table
print(table)
