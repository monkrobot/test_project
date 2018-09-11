##Алгоритм вставками
#def func1(N):
#    m = len(N)
#    for k in range(1, m):
#        for j in range(k, 0, -1):
#            if N[j] < N[j-1]:
#                N[j-1], N[j] = N[j], N[j-1]
#            else:
#                continue
#    return N
#
##Алгоритм выбором
#def func2(N):
#    m = len(N)
#    for i in range(m-1):
#        for k in range(i+1, m):
#            if N[k] < N[i]:
#                N[i], N[k] = N[k], N[i]
#    return N
#
##Алгоритм пузырек
#def func3(N):
#    m = len(N)
#    for k in range(m - 1):
#        for j in range(1, m - k):
#            if N[j] < N[j-1]:
#                N[j-1], N[j] = N[j], N[j-1]
#
#    return N
#
#def test_func(func):
#    N = [3,5,2,4,6]
#    ans = [2,3,4,5,6]
#    func_ans = func(N)
#    print("ok" if func_ans == ans else "fail")
#
#    N = [5, 5, 2, 6, 6, 3, 2]
#    ans = [2, 2, 3, 5, 5, 6, 6]
#    func_ans = func(N)
#    print("ok" if func_ans == ans else "fail")
#
#    N = list(range(10, 20)) + list(range(10))
#    ans = list(range(20))
#    func_ans = func(N)
#    print("ok" if func_ans == ans else "fail")
#
#if __name__ == "__main__":
#    for j in [func1, func2, func3]:
#        test_func(j)
#    print("_"*10)
#    print(func1(list(range(10, 20)) + list(range(10))))


#решето Эратосфена
import time

start = time.clock()
def func(N):
    '''N - число, до которого надо найти все простые числа'''
    assert N > 0, "Fail, N < 0"
    prost = [True]*N
    answer = [0, 1]
    #prost[0], prost[1] = True, True
    for k in range(2, len(prost)):
        if prost[k]:
            answer.append(k)
            for m in range(2*k, N, k):
                prost[m] = False
        else:
            continue
    print(answer)
    print(len(answer))
    print(time.clock() - start)


func(100)
