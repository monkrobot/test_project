import re

data = []

def check_empty(sentence):
    if '' in sentence:
        sentence.remove('')
        return check_empty(sentence)
    else:
        return sentence

with open('sentences.txt', 'r') as file:
    for line in file:
        sentence = re.split('[^a-z]', line.lower())
        check_empty(sentence)

        data.append(sentence)
        #for i in sentence:
        #    if i == []:
        #
print(data)