import json

data = json.load(open("dictionary.json"))
from difflib import get_close_matches


def retrive_definition(word):
    word = word.lower()

    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        action = input("Did you mean {} instead? [y or n]: ".format(get_close_matches(word, data.keys())[0]))
        if action == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif action == "n":
            return "The word doesn't exist, yet."
        else:
            return "We don't understand your entry. Apologies"
    else:
        return "The word doesn't exist, please double check it"



if __name__ == "__main__":
    word_user = input("Enter a word: ")

    output = retrive_definition(word_user)

    if type(output) == list:
        for item in output:
            print("-", item)
    else:
        print("-", output)
