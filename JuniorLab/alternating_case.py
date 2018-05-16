'''
В качестве аргумента функция принимает строку.
Верните строку, модифицировав ее таким образом, что бы каждая заглавная буква стала строчной,
а каждая строчная - заглавной
'''

N = "HeLLo WoRLD"
A = '132HeLLo41 WoRLD'

def func(n):
    answer = ''
    for i in n:
        if i.isdigit():
            answer += i
        elif i.isupper():
            answer += i.lower()
        else:
            answer += i.upper()
    return answer

print(func(N))