'''
Найдите наибольший общий делитель двух положительных целых чисел.
Числа могу быть очень большими, поэтому подходите к решению с умом.

Входящие аргументы x и y всегда больше или равны 1,
поэтому наибольший общий делитель всегда будет целым числом, которое больше или равно 1.
'''

#import time
#
#n = 1590771464
#m = 1590771620
#
#start = time.time()
#
##It works, but too slow
#def func(n,m):
#    if n > m:
#        max_num = n
#        min_num = m
#    else:
#        max_num = m
#        min_num = n
#    for i in range(1,min_num+1):
#        if min_num % i == 0:
#            max_dev = min_num / i
#            if max_num % max_dev == 0:
#                return int(max_dev)
#        else:
#            continue
#
#print(func(n,m))
#
#print(time.time()-start )


#Euclidean algorithm
import time

a = 30
b = 18
start = time.time()
def func(a,b):
    while a != 0 and b != 0:
        if a > b:
            a = a%b
        else:
            b = b%a
    return a+b
    #if a > b:
    #    maxnum = a
    #    minnum = b
    #else:
    #    maxnum = b
    #    minnum = a
    #if maxnum % minnum == 0:
    #    return minnum
    #else:
    #    return func(minnum, maxnum%minnum)

print(func(a,b))
print(time.time() - start)