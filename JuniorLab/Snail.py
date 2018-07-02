'''Вам дан массив n на n. Верните массив, в котором элементы расположены по следующему порядку:
от внешних элементов к центру по часовой стрелке.'''
import copy
array = [[1,2,3,4],
         [12,13,14,5],
         [11,16,15,6],
         [10,9,8,7]]
print(array)
def snail(array):
    answer = []
    left_side = []
    new_array = copy.copy(array)
    for circle in range(len(array)-1):
        for row in range(len(new_array)):
            #try:
                if row == 0:
                    #answer.append(new_array.pop(row))
                    answer.append(new_array[row])
                    #new_array[row] = []
                elif row == len(new_array) - 1:
                    #answer.append(sorted(new_array.pop(row)))
                    answer.append(sorted(new_array[row]))
                    answer.append(list(reversed(left_side)))
                    left_side = []
                    #new_array[row] = []
                else:
                    answer.append(new_array[row].pop(-1))
                    left_side.append(new_array[row].pop(0))
                    #new_array[row][-1] = []
                    #new_array[row][0] = []
            #except:
            #    continue
        try:
            new_array.pop(0)
            new_array.pop(-1)
        except:
            break
    return answer

print(snail(array))
print('array:', array)