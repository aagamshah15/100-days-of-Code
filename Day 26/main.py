import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
phonetic_data = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_data)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter your name: ").upper()
output_list = [phonetic_data[letter] for letter in word]
print(output_list)