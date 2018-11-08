'''
Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк,
заканчивающихся строкой, содержащей только строку "end" (без кавычек)

Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме
элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний
элемент находится с противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.
'''

matrix = []
while True:
    mat = input()
    if mat != 'end':

        matrix.append([int(x) for x in mat.split()])
    else:
        break
row = []
for _ in range(len(matrix[0])):
    row.append(0)

answer = []
for _ in range(len(matrix)):
    answer.append(row[:])
ans = 0

print('matrix: ', matrix)
print('answer: ', answer)



len_matr = len(matrix)
len_inn_matr = len(matrix[0])
for i in range(len_matr):
    for j in range(len_inn_matr):
        answer[i][j] = matrix[i-1][j] + matrix[i-len_matr+1][j] + matrix[i][j-1] + matrix[i][j-len_inn_matr+1]

for i in range(len_matr):
    for j in range(len_inn_matr):
        if j != len_inn_matr - 1:
            print(answer[i][j], end=' ')
        else:
            print(answer[i][j])





#if len(matrix) == 1 and len(matrix[0]) == 1:
#    for i in range(4):
#        ans += matrix[0][0]
#    print(ans)
#elif len(matrix) > 1 and len(matrix[0]) == 1:
#   for i in range(len(matrix)):
#        if i == 0:
#            answer[i][0] += matrix[i + 1][0] + matrix[-1][0] + matrix[i][0] + matrix[i][0]
#        elif i == len(matrix) - 1:
#            answer[i][0] += matrix[i - 1][0] + matrix[0][0] + matrix[i][0] + matrix[i][0]
#        else:
#            answer[i][0] += matrix[i - 1][0] + matrix[i + 1][0] + matrix[i][0] + matrix[i][0]
#   for i in range(len(answer)):
#       print(answer[i][0])
#elif len(matrix) == 1 and len(matrix[0]) > 1:
#   for i in range(len(matrix[0])):
#        if i == 0:
#            answer[0][i] += matrix[0][i + 1] + matrix[0][-1] + matrix[0][i] + matrix[0][i]
#        elif i == len(matrix[0]) - 1:
#            answer[0][i] += matrix[0][i - 1] + matrix[0][0] + matrix[0][i] + matrix[0][i]
#        else:
#            answer[0][i] += matrix[0][i - 1] + matrix[0][i + 1] + matrix[0][i] + matrix[0][i]
#   for i in range(len(answer[0])):
#       print(answer[0][i], end=' ')
#else:
#    for i in range(len(matrix)):
#        for j in range(len(matrix[i])):
#            if i == 0:
#                answer[i][j] += matrix[i + 1][j] + matrix[-1][j]
#            elif i == len(matrix) - 1:
#                answer[i][j] += matrix[i - 1][j] + matrix[0][j]
#            else:
#                answer[i][j] += matrix[i - 1][j] + matrix[i + 1][j]
#            if j == 0:
#                answer[i][j] += matrix[i][j + 1] + matrix[i][-1]
#            elif j == len(matrix[i]) - 1:
#                answer[i][j] += matrix[i][j - 1] + matrix[i][0]
#            else:
#                answer[i][j] += matrix[i][j - 1] + matrix[i][j + 1]
#
#    for i in range(len(answer)):
#        for j in range(len(answer[i])):
#            if j != len(answer) - 1:
#                print(answer[i][j], end=' ')
#            else:
#                print(answer[i][j])
#

