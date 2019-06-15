A = [2,2,3,4,3,3,2,2,1,1,2,2]

valley = 0
hill = 0

n = 0


#for i in [1, len(A)-1]:
#    if A[i] == A[i-1]:
#        continue
#    elif A[i] > A[i-1] and A[i] > A[i+1]:
#        hill += 1
#        print('hill: ', hill)
#    else:
#        valley += 1
#        print('valley: ', valley)

flag = 0

for i in range(len(A)-1):
    print(A[i])
    if A[i] == A[i+1]:
        continue
    elif A[i] > A[i+1] and flag <= 0:
        hill += 1
        n += 1
        flag = 1
        print('hill: ', hill)
    elif A[i] < A[i+1] and flag >= 0:
        valley += 1
        n += 1
        flag = -1
        print('valley: ', valley)

if A[len(A)-2] != A[len(A)-1] or flag == 0:
    n += 1

print('n', n)