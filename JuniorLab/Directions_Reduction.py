arr = [ 'NORTH', 'SOUTH','NORTH', 'SOUTH', 'EAST' ]

def dir_reduc(arr):
    EAST, WEST = 1, -1
    NORTH, SOUTH = 2, -2
    answer = []
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

    return(answer)

print(dir_reduc(arr))
