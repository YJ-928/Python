# importing csv module
import csv

# creating empty lists
Tempratures = []
Days = []
Conditions = []

# reading and extracting data into seperate lists
with open("12.weather_data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        if row[0] == "day" and row[1] == "temp" and row[2] == "condition":
            continue
        Days.append(row[0])
        Tempratures.append(int(row[1]))
        Conditions.append(row[2])

# printing out the extracted data
print(Days, Tempratures, Conditions)
