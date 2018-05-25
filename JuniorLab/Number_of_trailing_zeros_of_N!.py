'''
Нужно написать функцию, которая возвращает количество конечных нулей в факториале переданного числа.

N! = 1 * 2 * 3 * 4 ... N
'''

def zeros(n):
    fact = 1
    if n == 0:
        return 0
    for i in range(1, n+1):
        fact *= i
    for j in str(fact):
        print(j)

print(zeros(12))
