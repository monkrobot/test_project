#Find missed element in list
#100%

import time
l = []
N = 100000
for i in range(N):
    l.append(i+1)

start = round(time.time(), 50)
#Slowly
#def solution(A):
#    if A == []:
#        return []
#    for i in range(len(A)+1):
#        if i+1 in A:
#            continue
#        else:
#            return i+1

def solution(A):
    #if A == []:
    #    return []
    B = sorted(A)
    B.append(None)
    for i in range(len(A)+1):
        if i+1 == B[i]:
            continue
        else:
            return i+1

print(solution([])) #[2, 6, 7, 1, 8, 3, 5, 4, 9]

print('time is', round(time.time()-start, 50))