##Exercise 1
#
#import re
#import pandas as pd
#from scipy.spatial.distance import cosine
#
#data = []
#
#def check_empty(sentence):
#    if '' in sentence:
#        sentence.remove('')
#        return check_empty(sentence)
#    else:
#        return sentence
#
#words = {}
#columns = {}
#
#with open('sentences.txt', 'r') as file:
#    for line in file:
#        sentence = re.split('[^a-z]', line.lower())
#        check_empty(sentence)
#
#        data.append(sentence)
#        for i in sentence:
#            if i not in words:
#                words[i] = 1
#            else:
#                words[i] += 1
#
##print(data)
##print(words)
##print(len(words))
#
#for j,k in zip(range(len(words)), words):
#    columns[j] = k
##print(columns)
#
##print(len(columns))
#
#d = {}
#
#for i in range(len(columns)):
#    d[i] = [0] * len(data)
#
#for word in range(len(columns)):
#    for senten in range(len(data)):
#        for senten_word in data[senten]:
#            if columns[word] == senten_word:
#                d[word][senten] += 1
#
#frame = pd.DataFrame(d)
#print(frame)
#
#answer1 = []
#
#for senten in range(1, len(data)):
#    answer1.append(cosine(frame.loc[0], frame.loc[senten]))
#print(answer1)
#print(max(answer1))
#sort_answer1 = sorted(answer1)
#print('sort:', sort_answer1)
#print('sort_answer1[-2]', sort_answer1[-2])
#print('sort_answer1[-1]', sort_answer1[-1])
#print('index:', answer1.index(sort_answer1[-1]))
#print('index 0:', answer1[0])
#print('index 16:', answer1[16])
##print(answer1[16])
#print(data[answer1.index(sort_answer1[-1])])
#
##answers: index 0: 0.9527544408738466
##         index 16: 0.956644501523794


#Exercize 2
import math

def func1(x):
     f = math.sin(x/5)*math.exp(x/10)+5*math.exp(-x/2)
     return(f)
print(func1(1))
print(func1(5))

from scipy import linalg
import numpy as np

A = [[1,5,1],
     [4,2,6],
     [8,4,9]]

b = [[1],
     [8],
     [15]]

answer = linalg.solve(A,b)

print('answer:\n', answer)
print('np.dot(A, answer):\n', np.dot(A, answer))
