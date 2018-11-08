#Exercize 1
#import re
#import pandas as pd
#from scipy.spatial import distance
#
#
##def empty_word(sentence):
##    for word in sentence:
##        if word == '':
##            sentence.remove(word)
##            empty_word(sentence)
##    return sentence
#
#def empty_word(sentence):
#    '''
#    Take a list of words in sentence, delete empty words ""
#    Return a list of words in sentence without ""
#    '''
#    new_sentence = []
#    for word in sentence:
#        if word != '':
#            new_sentence.append(word)
#    return new_sentence
#
##def empty_word(sentence):
##    empty = sentence.count('')
##    for _ in range(empty):
##        sentence.remove('')
##    return sentence
#
#all_words = {}
#matrix = {}
#with open("sentences.txt", "r") as file:
#    sentence_num = 0
#    for line in file:
#        words = {}
#        sentence = re.split('[^a-z]', line.lower())
#        sentence = empty_word(sentence)
#
#        for word in sentence: #number of each word in sentence
#            #if word not in all_words:
#            #    all_words[word] = 0
#            if word not in words:
#                words[word] = 1
#            else:
#                words[word] += 1
#
#        matrix[sentence_num] = words
#        sentence_num += 1
#
#df = pd.DataFrame(matrix)
#df_matrix = df.T
#
#df_matrix.fillna(0, inplace=True)
#
##print(df_matrix)
#
#cos_ans = []
#for i in range(1, df_matrix.shape[0]):
#    print(distance.cosine(df_matrix.ix[[0]], df_matrix.ix[[i]]))
#    cos_ans.append(distance.cosine(df_matrix.ix[[0]], df_matrix.ix[[i]]))
#
#cos_ans = sorted(cos_ans)
#print('answer: ', cos_ans[-2:])

#Exercize 2

