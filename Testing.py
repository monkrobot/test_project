#Need to find the max product of three numbers in list

A = [1,2,-3]
#print(A.pop(A.index(max(A))))
print(A)

#88%

max1 = (A.pop(A.index(max(A))))
max2 = (A.pop(A.index(max(A))))
max3 = (A.pop(A.index(max(A))))
if len(A) >= 2:
    min1 = (A.pop(A.index(min(A))))
    min2 = (A.pop(A.index(min(A))))
    if min1*min2*max1 < max1*max2*max3:
        maxProd = max1 * max2 * max3
    else:
        maxProd = min1 * min2 * max1
else:
    maxProd = max1 * max2 * max3



print(maxProd)

# 44%
#maxProd = - float('inf')
#
#for i in range(len(A)-2):
#    for j in range(i+1,len(A)-1):
#        for k in range(j+1,len(A)):
#            maxProdTry = A[i] * A[j] * A[k]
#            if maxProd < maxProdTry:
#                maxProd = maxProdTry
#                print(A[i], A[j], A[k])
#                print(maxProd)
#
#print('result: ', maxProd)
