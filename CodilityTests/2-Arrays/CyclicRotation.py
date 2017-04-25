def solution(A, K):
    if A == []:
        B = A
        return B
    else:
        for i in range(K):
            B = A[:-1]
            print(B)
            B.insert(0, A[-1])
            print('B.insert(0, A[-1])', B)
            A = B
        return B

A = [2]
print(solution(A, 5))