#Find element, which doesn't repeated
#problems with work speed 66%

def solution(A):
    B = A[1:]
    element = A[0]
    print('B:', B)
    print('element:', element)
    if B == []:
        return element

    try:
        element_to_del = B.index(element)
        del B[element_to_del]
        return solution(B)
    except:
        return element


print(solution([39, 21, 21, 1, 39, 1, 9]))
