#Find the quantity of numbers, which divisioned by K whithout excess(остаток) / simple sivisioned by K.
#Numbers between A and B

import time

#Try 1 - Problems with speed 50%
#start = time.time()
#
#def solution(A, B, K):
#    array_b = [0]*(B+1-A)
#    help_number = A
#    result = 0
#    for i in range(B+1-A):
#        array_b[i] = help_number
#        help_number += 1
#        #print('array_b:', array_b[i])
#        #print('result:', result)
#        #print('/', array_b[i]%K)
#        if array_b[i] % K == 0:
#            result += 1
#
#    return result
#
#print(solution(10,12300000,2))
#
#print('time is:', time.time()-start)


#Try 2 - Problems with speed and correctness 37%
start = time.time()

def solution(A, B, K):
    if A <= K:
        help_number = K
        print('help_number', help_number)
    elif A % K == 0:
        help_number = A
        print('help_number', help_number)
    #elif A//K == 1:
    #    help_number = (A // K + 1) * K
    #    print('help_number', help_number)
    else:
        help_number = (A // K + 1) * K
        print('help_number', help_number)
    result = 0
    while 0 <= help_number <= B:
        result += 1
        help_number += K
    #for i in range(B+1-A):
    #    array_b[i] = help_number
    #    help_number += 1
    #    #print('array_b:', array_b[i])
    #    #print('result:', result)
    #    #print('/', array_b[i]%K)
    #    if array_b[i] % K == 0:
    #        result += 1

    return result

print(solution(121,121000000,2))

print('time is:', time.time()-start)