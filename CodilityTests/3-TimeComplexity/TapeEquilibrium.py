#Find a minimal result of slices sum(A[:(P + 1)]) - sum(A[(P + 1):])
#problems with work speed 50%

#import math
#def solution(A):
#    minimal = float('inf')
#    for P in range(len(A)-1):
#        print(A[:(P+1)])
#        print(A[(P+1):])
#        if minimal > math.fabs(sum(A[:(P + 1)]) - sum(A[(P + 1):])):
#            minimal = math.fabs(sum(A[:(P + 1)]) - sum(A[(P + 1):]))
#            print('minimal',minimal)
#        else:
#            continue
#    return minimal

def solution(A):

    minimal = float('inf')
    print('minimal is here:',minimal)
    for P in range(len(A)-1):
        print(A[:(P+1)])
        print(A[(P+1):])
        print('summa all', sum(A[:(P + 1)]) - sum(A[(P + 1):]))
        if minimal > abs(sum(A[:(P + 1)]) - sum(A[(P + 1):])):
            minimal = abs(sum(A[:(P + 1)]) - sum(A[(P + 1):]))
            print('minimal', minimal)
        else:
            continue
    return minimal

A = [100, -100]
print('solution is: ', solution(A))
print('sumA', sum(A))


K = [1,2,3,4]
for i in range(len(K)-1):
    print(i+1)
print('K is', K[:3])