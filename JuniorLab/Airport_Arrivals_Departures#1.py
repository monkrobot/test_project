'''
Каждый символ управляется с помощью ротора, а порядок символов на каждом роторе следующий:
ABCDEFGHIJKLMNOPQRSTUVWXYZ ?!@#&()|<>.:=-+*/0123456789

Дисплей работает по следующим правилам:
Начиная с левого края (от текущего символа до конца линии) все значения меняются,
пока символ левого ротора не будет правильным.
Затем механизм переходит на один ротор вправо.
Повторяет шаг первый. И так до тех пор, пока вся строка не будет обновлена.
Вся процедура повторяется сверху вниз, пока все табло не будет обновлено.
функция flapDisplay принимает два аргумента: массив слов и массив смещений.

Задача:
Написать метод, который вернет массив со строкой, полученной после смещений символов на указанные значения.
'''

lines = ["NOTHING MOVED"]
rotors = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def flap_display(lines, rotors):
    seq = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ?!@#&()|<>.:=-+*/0123456789"
    answer = [x for x in lines[0]]
    print(answer)
    print('answer1', answer)
    for rot in range(len(rotors[0])):
        for i in range(rot, len(answer)):
            if seq.index(answer[i]) + rotors[0][rot] < len(seq):
                print('letter:', answer[i])
                print(seq.index(answer[i]) + rot)
                print('seq', seq.index(answer[i]))
                answer[i] = seq[seq.index(answer[i]) + rotors[0][rot]]
                print('answer:', answer)
            else:
                answer[i] = seq[seq.index(answer[i]) + rotors[0][rot] - len(seq)]
    return [''.join(answer)]

print(flap_display(lines, rotors))