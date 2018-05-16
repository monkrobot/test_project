'''
Нужно прийти из одной точки к другой. Нужно оставить только те направления, которые имеют смысл.

Если дан маршрут ["EAST", "WEST"], то "EAST" и "WEST" гасят друг друга.
Нет смысла вообще двигаться с места, поэтому результатом будет пустой массив []
Не все пути можно упростить. Например, путь ["NORTH", "WEST", "SOUTH", "EAST"] не упрощается.
"NORTH" и "WEST", "WEST" и "SOUTH", "SOUTH" и "EAST" не прямо противоположны друг другу.
Значит результатом будет: ["NORTH", "WEST", "SOUTH", "EAST"].
'''

arr = [ 'NORTH', 'NORTH', 'NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'WEST' ]

def dir_reduc(arr):
    EAST, WEST = 1, -1
    NORTH, SOUTH = 2, -2
    answer = []
    if len(arr) == 1:
        answer.append(arr[0])
        return answer
    for i in range(len(arr)-1):
        l = locals()
        exec('num =' + arr[i])
        exec('num1 =' + arr[i+1])
        n = l['num']
        m = l['num1']
        if arr[i] == '0':
            continue
        elif n + m != 0:
            answer.append(arr[i])
            if i == len(arr)-2:
                answer.append((arr[i+1]))
        else:
            arr[i], arr[i+1] = '0', '0'
            if i+1 == len(arr)-2:
                answer.append((arr[i + 2]))
            continue
    if arr == answer:
        return answer
    else:
        return dir_reduc(answer)


#def dir_reduc(arr):
#    EAST, WEST = 1, -1
#    NORTH, SOUTH = 2, -2
#    l = locals()
#    exec('num =' + arr[0])
#    exec('num1 =' + arr[1])
#    n = l['num']
#    m = l['num1']
#    if n + m != 0:
#        if arr.index(arr[0]) == len(arr) - 2:
#            return arr[0] + arr[1]
#        return arr[0] + dir_reduc(arr[1:])
#    else:
#        arr[i], arr[i+1] = '0', '0'
#        if i+1 == len(arr)-2:
#            answer.append((arr[i + 2]))
#        continue
#
#    return(answer)

print(dir_reduc(arr))
