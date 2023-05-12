import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phenotic_dict = {row.letter:row.code for (index,row) in data.iterrows()}

while True:
    try:
        user_name = input("Enter your Name: ").upper()
        user_nato_alphabets = [phenotic_dict[letter] for letter in user_name if letter != " "]
    except KeyError:
        print("Sorry, only letters in alphabet please")
    else:
        break
    
print('\n',user_nato_alphabets,'\n')
