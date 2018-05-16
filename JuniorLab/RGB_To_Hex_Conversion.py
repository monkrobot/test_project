'''
Допишите функцию rgb(). В качестве аргументов она принимает десятичные значения RGB.
Функция должна вернуть значение цвета в шестнадцатеричном формате.
Допустимые значения RGB в десятичном формате равны 0-255. Если числа выходят за указанный диапазон,
то нужно округлить их до ближайшего возможного числа. Ниже приведены примеры.
'''

n = 15
print(str(hex(n)))
print(int('ff', 16))

def rgb(red, green, blue):
    result = ''
    for i in [red, green, blue]:
        if i < 0:
            color = '00'
        elif i < 16:
            color = '0' + str(hex(i))[2:]
        elif i > 255:
            color = str(hex(255))[2:]
        else:
            color = str(hex(i))[2:]
        result += color.upper()
    return result

print(rgb(255, 11, 298))