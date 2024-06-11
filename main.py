import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass


student_data_frame = pd.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

nato = pd.read_csv("nato.csv")
nato_dict = {row.letter: row.code for (index, row) in nato.iterrows()}
print(nato_dict)
# print(nato)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# adding error handling to input
while True:
    word = input("Enter a word: ").upper()
    try:
        letters = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters of the alphabet please.")
    else:
        print(letters)
        break

