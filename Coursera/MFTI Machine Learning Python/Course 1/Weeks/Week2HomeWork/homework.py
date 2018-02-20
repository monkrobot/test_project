import re
import pandas as pd
import numpy as np

data = []

def check_empty(sentence):
    if '' in sentence:
        sentence.remove('')
        return check_empty(sentence)
    else:
        return sentence

words = {}
columns = {}

with open('sentences.txt', 'r') as file:
    for line in file:
        sentence = re.split('[^a-z]', line.lower())
        check_empty(sentence)

        data.append(sentence)
        for i in sentence:
            if i not in words:
                words[i] = 1
            else:
                words[i] += 1

#print(data)
#print(words)
#print(len(words))

for j,k in zip(range(len(words)), words):
    columns[j] = k
#print(columns)

print(len(columns))

d = {}

for i in range(len(columns)):
    d[i] = [False] * len(data)

for word in range(len(columns)):
    for senten in range(len(data)):
        if columns[word] in data[senten]:
            d[word][senten] = True

frame = pd.DataFrame(d)
print(frame)

