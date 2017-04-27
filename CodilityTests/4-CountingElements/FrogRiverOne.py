#Find index of X in A
#18% I don't understand the quize

def solution(X, A):
    if X in A:
        return A.index(X)
    else:
        return -1

B = [x for x in range(-1500, 10000)]
A = [4,9,2,1]
print(solution(128,B))