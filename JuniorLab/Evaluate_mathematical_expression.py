'''
Принимая в качестве входного аргумента математическое выражение, вы должны вычислить его и вернуть результат.

Числа могут быть как целыми, так и дробными. Это касается как чисел в выражении так и результата.

Вам могут встретиться следующие математические операторы.

Умножение *
Деление /
Сложение +
Вычитание -
В выражении может быть несколько уровней вложенности скобок.

Выражение может содержать пробелы между числами и операторами.

Знак минус, обозначающий отрицание числа или выражения в скобках, никогда не будет отделен пробелом.
'''
def func1(n):
    l = locals()
    exec('m =' + n)
    m = l['m']
    return m

print(func1('6 + -( -4)'))
