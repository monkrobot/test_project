'''
Напишите функцию так, чтобы она преобразовывала строку в которой слова разделены
с помощью тире / подчеркивания в строку, которая записана по правилам camelCase.
'''

n = "the-stealth-warrior"
m = "The_Stealth_Warrior"
a = ''

if '-' in m:
    print('Yes')

def func(n):
    if '_' in n:
        new_list = n.split('_')
    elif '-' in n:
        new_list = n.split('-')
    else:
        return n
    result = new_list[0]
    for i in new_list[1:]:
        result += i.capitalize()
    return(result)

print(func(n))