import pandas

data = pandas.read_csv("16.Central_Park_Squirrel_Data.csv")

# TODO-1: Extract all Squirrels based on their Fur color and
# create new csv file using that data
Cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
Gray = len(data[data["Primary Fur Color"] == "Gray"])
Black = len(data[data["Primary Fur Color"] == "Black"])

print(
    f"There are Cinnamon: {Cinnamon}, Gray: {Gray}, Black: {Black} Squirrels")

squirrel_fur_data = {
    "Fur Color": ["Cinnamon", "Gray", "Black"],
    "Count": [Cinnamon, Gray, Black],
}

data_fur = pandas.DataFrame(squirrel_fur_data)
data_fur.to_csv("16.Squirrel_Fur_Data.csv")
