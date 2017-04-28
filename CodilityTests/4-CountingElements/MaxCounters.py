#https://codility.com/c/run/trainingGBBR3C-SA8
#problems with work speed 66%
import time

A = [1,4,3,6,2,3,1,4,2,5,5,3,1,1]*1000000
start = time.time()

def solution(N, A):
    counters = [0] * N
    for i in A:
        #print('i', i)
        if 0 < i <= N:
            counters[i-1] += 1
            #print('counters', counters)
        elif i == N+1:
            counters = [max(counters)] * N
            #print('counters *max', counters)
        else:
            continue
    return counters

print(solution(5, A))

print('time:', time.time()-start)
