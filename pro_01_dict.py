# Importing libraries
import json
from difflib import get_close_matches

# Importing data
data = json.load(open('data.json'))


# Function for getting word-meaning
def meaning(word_f):
    word_f = word_f.lower()                                          # To remove case-sensitive problems(due to input)
    matches = get_close_matches(word_f, data.keys(), cutoff=0.8)[0]  # Close matching word with highest matching ratio
    if word_f in data:                  # Simple words
        return data[word_f]
    elif word_f.title() in data:        # Important words ( eg- Delhi, America etc)
        return data[word_f.title()]
    elif word_f.upper() in data:        # For acronyms ( eg- USA, NATO etc)
        return data[word_f.upper()]
    elif matches:                       # Close matching words
        choice = input("Did you mean '{}'? \n'Y' for yes or 'N' if no: ".format(matches))
        if choice.lower() == 'y':
            return data[matches]
        elif choice.lower() == 'n':
            return "Word doesn't exist. Please double check it."
        else:
            return "Invalid entry."
    else:                               # Invalid words
        return "Word doesn't exist. Please double check it."


# Input word
word = input("Enter a word: ")

# Output meaning
output = meaning(word)
if type(output) == list:
    for item in output:
        print("** " + item)
else:
    print(output)
