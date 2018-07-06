'''Вам дан массив n на n. Верните массив, в котором элементы расположены по следующему порядку:
от внешних элементов к центру по часовой стрелке.'''

#array = [[1,2,3,4],
#         [12,13,14,5],
#         [11,16,15,6],
#         [10,9,8,7]]

array = [[1]]

def snail(array):
    answer = []
    left_side = []
    new_array = array[:]
    for circle in range(len(array)):
        for row in range(len(new_array)):
                if row == 0:
                    answer.extend(new_array[row])
                elif row == len(new_array) - 1:
                    answer.extend(reversed(new_array[row]))
                    if left_side:
                        answer.extend(list(reversed(left_side)))
                        left_side = []
                else:
                    answer.append(new_array[row].pop(-1))
                    left_side.append(new_array[row].pop(0))
        try:
            new_array.pop(0)
            new_array.pop(-1)
        except:
            break
    return answer

print(snail(array))