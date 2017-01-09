import copy

n = 5
diag = n*2 - 1
numbers = n*n
previous = 0
k_previous = 0

matrix = []
under_matrix = []

for j in range(1, n + 1):
    under_matrix.append(None)

for i in range(1, n+1):
    matrix.append(copy.copy(under_matrix))

for iteration in range(1, diag+1):
    if iteration <= diag / 2 + 1:
        j = n - iteration
        k = 0
        while k < iteration:
            number = previous + 1
            matrix[k][j] = number
            print(matrix)
            previous = number
            j += 1
            k += 1
    else:
        k = 1 + k_previous
        j = 0
        k_previous = k
        while k < n:
            number = previous + 1
            matrix[k][j] = number
            previous = number
            print(matrix)
            j += 1
            k += 1
for m in range(0,n):
    print(matrix[m])
