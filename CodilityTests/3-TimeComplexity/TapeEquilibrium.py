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

    minimal = sum(A) #not equal to sum(A). It's a mistake in list with numbers lower than 0
    for P in range(len(A)-1):
        print(A[:(P+1)])
        print(sum(A[:(P + 1)]))
        print(A[(P+1):])
        print('summa all', sum(A[:(P + 1)]) - sum(A[(P + 1):]))
        if minimal > sum(A[:(P + 1)]) - sum(A[(P + 1):]):
            minimal = sum(A[:(P + 1)]) - sum(A[(P + 1):])
            print('minimal', minimal)
        else:
            continue
    return minimal

A = [100, -1, -8, 5, -10]
print(solution(A))
print('sumA', sum(A))