'''
Вам даны две величины:
Длина прямоугольника (параметр lng)
Ширина прямоугольника (параметр width)
Вы должны вернуть массив чисел с размером стороны каждого квадрата.

Если передаваемые аргументы равны, то вернуть null.
'''

lng = 3
width = 5

def func(lng, width):
    answer = []
    if lng == width:
        return "null"

    if lng < width:
        cap = lng
        lng = width
        width = cap

    while lng != 0:
        if width < lng:
            answer.append(width)
            lng = lng - width
        elif lng == 1:
            for _ in range(width):
                answer.append(1)
            lng = 0
        elif width > lng:
            cap = lng
            lng = width
            width = cap
        else:
            answer.append(width)
            return answer
    return answer

print(func(lng,width))
