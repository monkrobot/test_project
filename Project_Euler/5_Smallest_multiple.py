'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

#import time
#
#start = time.clock()
#N = 30
## This solution is not good
#for i in range(232792560, 10000000000000000, N):
#
#    for j in [4,7,8,9,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29]:
#        #print('i:', i)
#        if i % j == 0:
#            continue
#        else:
#            #print('break on', j)
#            break
#    else:
#        print('answer:', i)
#        break
#
#print(time.clock() - start)

from math import log

N = 20
def func(N):
    '''N - число, до которого надо найти все простые числа'''
    assert N > 0, "Fail, N < 0"
    prost = [True]*N
    answer = []
    for k in range(2, len(prost)):
        if prost[k]:
            answer.append(k)
            for m in range(2*k, N, k):
                prost[m] = False
        else:
            continue
    return answer

prost_number = func(N)
solution = 1
print(prost_number)
#print(log(32, 2))
for i in prost_number:
    #print('N: ', N)
    #print("i: ", i)
    solution *= i**(log(N, i))

print(solution)
