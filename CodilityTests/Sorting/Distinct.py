'''Find the distinct numbers in array A'''
#100%

import random

A = []
n = 12

for k in range(n):
    newk = random.randrange(1, 10)
    A.append(newk)

print('A: ', A)

#my solve
B = sorted(A)
B.append(-10)
print(B)
C = []
for i in range(1, len(B)-1):
    if B[i] != B[i+1]:
        C.append(B[i])
    else:
        continue

print(C)

#Solve
#B = sorted(A)
#print(B)
#C = [0]
#result = 1
#for i in range(1, len(B)):
#    if B[i] != B[i-1]:
#        C.append(B[i])
#        result += 1
#    else:
#        continue
#
#print(C)
#print(result)
