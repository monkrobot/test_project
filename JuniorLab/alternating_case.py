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