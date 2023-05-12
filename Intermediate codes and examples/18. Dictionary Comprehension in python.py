# NOTE: Syntax
# new_dict = {key:value for key,value in my_dict.items()}
# new_dict = {k:v for k,v in my_dict.items() if condition=True/False}
import pandas
import random

new_dict = {key: random.randint(1, 100) for key in range(1, 100)}
print(new_dict)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
