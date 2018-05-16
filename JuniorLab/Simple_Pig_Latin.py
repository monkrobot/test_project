'''
Переместите первую букву в каждом слове в конец и добавьте 'ay'.
'''

n = "Pig latin is cool"

def func(n):
    ent_str = n.split(' ')
    pig_str = []
    for i in ent_str:
        pig_word = i[1:] + i[0] + 'ay'
        pig_str.append(pig_word)
    return ' '.join(pig_str)

print(func(n))
