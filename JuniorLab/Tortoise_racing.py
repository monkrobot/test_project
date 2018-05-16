'''
Даны две скорости v1 (Скорость черепахи A, v1 > 0) и v2 (Скорость черепахи B, v2 > 0) и расстояние между ними g.
Через сколько они встретятся?
Результат должен быть массивом [часы, минуты, секунды], который содержит часы минуты и секунды.
Если v1 >= v2 тогда нужно вернуть null, None в зависимости от языка.
'''

v1 = 720
v2 = 850
d = 70

def func1(v1,v2,d):

    if v2 <= v1:
        return None
    else:
        k = (v2 - v1)
        x1,x2 = divmod(d,k)
        print("x2:", x2)
        y1,y2 = divmod(x2*60, k)
        print("y2:", y2)
        z1 = divmod(y2 * 60, k)
        return [x1, y1, z1[0]]

def func(v1,v2,d):

    if v2 <= v1:
        return None
    else:
        x = d // (v2 - v1)
        y = d % (v2 - v1) / (v2 - v1) * 60
        print("Y:")
        print(y/60)
        print(y)
        z = y % int(y) * 60
        print("Z:")
        print(z/60)
        print(z)
        return [x, int(y), int(z)]

print(func1(v1,v2,d))
print(func(v1,v2,d))
