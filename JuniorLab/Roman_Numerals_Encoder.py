'''
Напишите функцию, которая переводит число, записанное арабскими цифрами в число, записанное римскими цифрами.
В качестве входного параметра передается положительное целое число. Возвращать функция должна строку с римским числом.
'''

number = 189


def solution(number):
    letters = {0: ['I', 'V'], 1: ['X', 'L'], 2: ['C', 'D'], 3: ['M']}
    answer = []

    for i in range(len(str(number))):
        numb = int(list(reversed(str(number)))[i])
        if i >= len(letters)-1:
            answer.extend(letters[3]*numb)
        else:
            if numb == 0:
                continue
            elif numb <= 3:
                answer.extend([letters[i][0]*numb])
            elif numb == 4:
                answer.extend([letters[i][1], letters[i][0]])
            elif numb == 5:
                answer.append(letters[i][1])
            elif numb <= 8:
                answer.extend([letters[i][0] * (numb - 5), letters[i][1]])
            elif numb == 9:
                answer.extend([letters[i + 1][0], letters[i][0] ])
    return ''.join(reversed(answer))

print(solution(number))
