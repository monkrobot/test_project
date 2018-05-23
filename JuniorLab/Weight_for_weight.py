'''
В качестве параметра функция принимает строку, содержащую числа, которые записаны через пробел.
Функция должна вернуть строку с этими же числами, но отсортированными в порядке возрастания по сумме цифр в числе.
Если два числа имеют одинаковый вес, то сортировать данные числа между собой надо так, как сортировали бы строки.
"56 65 74 100 99 68 86 180 90" -> "100 180 90 56 65 74 68 86 99"
'''

import re

#n = "56 65 74 100 99 68 86 180 90"
#new_n = n.split(' ')
#new_numbers = []
#
#for i in new_n:
#    new_m = 0
#    for j in i:
#        new_m += int(j)
#    new_numbers.append(new_m)
#
#print(new_numbers)



#n = "2000 10003 1234000 44444444 9999 11 11 22 123"
##"11 11 2000 10003 22 123 1234000 44444444 9999"
#
#def orderweight(str):
#    new_str = str.split(' ')
#    new_numbers = []
#
#    for i in new_str:
#        new_m = 0
#        for j in i:
#            new_m += int(j)
#        new_numbers.append(new_m)
#
#    dict_number = {x: y for x,y in zip(new_str, new_numbers)}
#    sort_new_numbers = sorted(new_numbers)
#    print('dict_number:', dict_number)
#
#    answer = []
#    for i in sort_new_numbers:
#        for key in dict_number:
#            if i == dict_number[key]:
#                answer.append(key)
#                dict_number[key] = 0
#    str_ans = ' '.join(answer)
#    return str_ans
#
#print(orderweight(n))



n = "101798 38 189482 8 212143 32 453748 180 247782 134 321210 35 342441 182 268273 176 245559 184 9175 30 68"
#"30 32 134 35 8 180 321210 182 38 184 212143 176 68 342441 9175 101798 268273 245559 247782 453748 189482"

def orderweight(str):
    new_numbers = []
    new_str = str.split(' ')

    for i in new_str:
        new_m = 0
        for j in i:
            new_m += int(j)
        new_numbers.append(new_m)

    dict_number = {}
    answer = ''
    for x,y in zip(new_numbers,new_str):
        if x in dict_number:
            dict_number[x].append(y)
        else:
            dict_number[x] = [y]
    for key in sorted(dict_number):
        answer += ' ' + ' '.join(sorted(dict_number[key]))
    return answer.lstrip()

print(orderweight(n))
