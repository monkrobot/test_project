'''
Английский алфавит содержит 26 букв: a = 1, b = 2 ... z = 26. Найдите максимальное значение,
которое получается путем сложения номеров подряд идущих согласных. Приведем пример.
Слово zodiacs содержит следующие подстроки согласных: z, d, cs.
Сумма этих подстрок равна соответственно 26, 4, 22 т.к. z = 26, d = 4, cs = 3 + 19 = 22.
Максимальное значение среди этих цифр равно 26. Соответственно функция должна вернуть 26.
'''

s = "chruschtschov"

def solve(s):
    alpha = {}
    for code,numb in zip(range(ord('a'), ord('z')+1), range(1,100)):
        alpha[chr(code)] = numb

    vowel = ['a', 'e', 'i', 'o', 'u', 'y']
    letter_weight = 0
    answer = 0
    for i in s:
        if i not in vowel:
            letter_weight += alpha[i]
        else:
            if letter_weight > answer:
                answer = letter_weight
                letter_weight = 0

    return answer

print(solve(s))
