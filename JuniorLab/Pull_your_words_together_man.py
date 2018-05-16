'''
Given a list of words. Need to concatanate words together in sentence with capitalized first word
and a dot in the end

Предложение должно начинаться с заглавной буквы.
В конце предложения должна стаять точка.
Между словами должен быть пробел.
Не выполняйте никаких других действий над словами.
'''

def sentencify(text):
    if not text[0][0].istitle():
        text[0] = text[0].capitalize()
    sentence = ''
    for x in text:
        sentence += x + ' '
    sentence = sentence[0:len(sentence)-1] + '.'
    return sentence





text = ['HELLO','world','good', 'buy']

print(sentencify(text))
