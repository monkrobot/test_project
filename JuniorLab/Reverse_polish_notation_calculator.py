'''
Reverse Polish notation. More information: https://en.wikipedia.org/wiki/Reverse_Polish_notation
For example: 5 1 2 + 4 * + 3 is equivalent to 5 + ((1 + 2) * 4) - 3
Symlols are divided by space, if not the expression is not valid
Empty string returns 0
Math symbols: + - * /.
'''

expr = "1 2 + 3 + 3.5 -"

def calc(expr):
    if len(expr) == 0:
        return 0
    expression = expr.split(' ')
    symbol = ['+', '-', '*', '/']
    answer = []
    print(expression)

    for i in expression:
        if i.isdigit():
            print('i:', i)
            answer.append(int(i))
        elif i in symbol:
            l = locals()
            exec('a =' + str(answer[-2]) + i + str(answer[-1]))
            answer.pop(-2)
            answer.pop(-1)
            a = l['a']
            answer.append(a)
        else:
            try:
                print('i:', i)
                answer.append(float(i))
            except:
                return "Not Valid"
    if len(answer) > 1:
        return answer[-1]
    return answer[0]

print(calc(expr))
