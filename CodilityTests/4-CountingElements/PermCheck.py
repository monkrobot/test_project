#Permutation - in list must be all elements from 1 to N without repeat
#100%

def solution(A):
    B = sorted(A)
    if B[-1] != len(B):
        print('oops')
        return 0
    else:
        for i in range(len(B)):
            print('i:', i)
            print('B[i]:', B[i])
            if B[i]==i+1:
                continue
            else:
                return 0
        return 1

print(solution([3,1,2,6,2,5]))