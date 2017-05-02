#Find all pairs of 0 and 1 in A from left to the right
#100%

def solution(A):
    result = 0
    gain = 1
    if 0 in A:
        j = A.index(0)
    else:
        return 0
    for i in A[j+1:]:
        if i != A[j]:
            result += gain
        else:
            gain += 1
    if result > 1000000000:
        return -1
    else:
        return result

A = [0, 1]
print(solution(A))