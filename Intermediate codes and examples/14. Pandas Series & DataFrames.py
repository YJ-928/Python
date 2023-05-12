import pandas

# NOTE:- here data is a DataFrame (df) in pandas
# consider it as an actual table
data = pandas.read_csv("12.weather_data.csv")
print(type(data))

# NOTE:-the indiviual cols of the data as called Series
days = data["day"]
print(type(days))
temp = data["temp"].to_list()  # to directly convert it to a list
conditions = data["condition"]

# NOTE:- calculating Average temprature
# average_temp = round(sum(temp) / len(temp), 2)
# Or can cal average using pandas
average_temp = data["temp"].mean()
print(f"Average Temp from data is:{average_temp} Degree Celcius")

# NOTE:- to fetch Max and min Temp values
# using Pandas Series in-built methods
print(f"Max temp: {data['temp'].max()} and Min temp: {data['temp'].min()}")

# NOTE:- fteching entire row, where the temp was Max
# instead of Sq Brakects we can work with,
# dot(.) also treating the data as an object
print(data[data.temp == data["temp"].max()])

# NOTE:- coverting data of temp from Celcius --> Farenheit
# 0deg --> (0°C × 9/5) + 32 = 32°F
# for monday
monday = data[data.day == "Monday"]
Temp = int(monday.temp)
print(f"Temp of Monday in Farenheit: {(Temp*(9/5))+32} deg F")
