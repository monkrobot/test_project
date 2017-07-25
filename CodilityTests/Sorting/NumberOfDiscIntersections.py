
#A = [1, 5, 2, 1, 4, 0]
A = [1,2,1,4]
b = [0]*len(A)
#print(b)
# 6%
for i in range(len(A)):
    b[i] += 1
    for j in range(1, A[i]+1):
        print('i:' + str(i) +' j:' + str(j) + ' b: ' + str(b))
        if i-j >= 0:
            b[i - j] += 1

        print('i:' + str(i) + ' j:' + str(j))

        if i + j < len(b):
            b[i + j] += 1

        print(b)
        print('-'*10)

print(b)
print(sum(b)//2)
