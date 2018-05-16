'''
Вам дан массив с числами. Нужно найти целое число, которое встречается нечетное число раз.
Такое число всегда будет только одно.
'''

N = [ 20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5, 20, 20, 20, 20 ]

def func(n):
    counter = {}
    for elem in n:
        counter[elem] = counter.get(elem, 0) + 1
    print(counter)
    for key in counter:
        if counter[key] % 2 != 0:
            return key

    #doubles = {element: count for element, count in counter.items() if count > 1}

print(func(N))