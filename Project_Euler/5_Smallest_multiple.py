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

N = 30

