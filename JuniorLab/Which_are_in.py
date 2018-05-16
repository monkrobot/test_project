'''
На вход в качестве аргументов передаются два массива a1 и a2.
Нужно вернуть массив r, который содержит отсортированные в лексикографическом порядке строки массива a1,
которые являются подстроками строк массива a2
'''

a1 = ["live", "arp", "strong"]
#a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
a2 = ["lovely", "interesting", "arjpose"]

def strfunc(a1, a2):
    a = sorted(a1)
    answer = []
    for word in a:
        for seq in a2:
            if word in seq:
                answer.append(word)
                break
            else:
                continue
    return answer

print(strfunc(a1,a2))
