import pandas

data_dict = {
    "students": ["Yash", "Angela", "raj"],
    "marks": [100, 9, 99],
}

data = pandas.DataFrame(data_dict)
data.to_csv("15.new_data.csv")
