import pandas
#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

nato_phonetic = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet = {value.letter: value.code for (key, value) in nato_phonetic.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_value = input("Enter a word: ").upper()
input_value = [nato_alphabet[letter] for letter in user_value]
print(input_value)