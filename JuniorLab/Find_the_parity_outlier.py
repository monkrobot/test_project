N = [2,4,0,0,0,3,98,-22]
A = [0, 3, 1719, 19, 11, 13, -21]

def func(n):
    answer = [x for x in n if x%2 == 0]
    if len(answer) == 1:
        return answer[0]
    else:
        answer = [x for x in n if x % 2 != 0]
        return answer[0]

print(func(A))