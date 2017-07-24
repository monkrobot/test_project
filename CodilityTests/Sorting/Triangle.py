#Find 3 numbers in A, such as everyone of them was lower than others sum

A = [-4, 2, -5, 1, 8, 20]
B = sorted(A)
result = 0
for k in range(1,len(B)-1):
    if B[k] + B[k - 1] > B[k + 1] and B[k] + B[k + 1] > B[k - 1] and B[k + 1] + B[k - 1] > B[k]:
        print('K: ', B[k-1], B[k], B[k+1])
        result = 1
        break
    else:
        continue
print(result)