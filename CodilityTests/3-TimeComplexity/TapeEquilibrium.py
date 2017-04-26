#import math
#def solution(A):
#    minimal = sum(A)
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
    minimal = sum(A)
    for P in range(len(A)-1):
        print(A[:(P+1)])
        print(A[(P+1):])
        if sum(A[:(P + 1)]) - sum(A[(P + 1):]) > 0:
            B = sum(A[:(P + 1)]) - sum(A[(P + 1):])
        else:
            B = sum(A[(P + 1):]) - sum(A[:(P + 1)])

        if minimal > B:
            minimal = B
            print('minimal',B)
        else:
            continue
    return minimal

A = [100, 1, 200, 4, 103]
print(solution(A))