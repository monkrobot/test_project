#25%
S = "CAGCCGA"
P = [2,5,0]
Q = [4,5,6]

#Big problems with time of work 62%
#def solution(S, P, Q):
#    """S - string DNA information, P and Q - arrays with numbers"""
#    dict_DNA = {'A': 1, 'C': 2, 'G': 3, 'T':4}
#    result = []
#    number_list_S = []
#    for dna in list(S):
#        #if dna in dict_DNA:
#        number_list_S.append(dict_DNA[dna])
#
#    for i in range(len(P)):
#        if P[i] != Q[i]:
#            slice_result = number_list_S[P[i]:Q[i]+1]
#            print('slice_result', slice_result)
#            result.append(min(slice_result))
#        else:
#            slice_result = number_list_S[P[i]]
#            print('slice_result', slice_result)
#            result.append(slice_result)
#        print(result)
#
#solution(S,P,Q)

#Big problems with time of work 62%
#def solution(S, P, Q):
#    """S - string DNA information, P and Q - arrays with numbers"""
#    dict_DNA = {'A': 1, 'C': 2, 'G': 3, 'T':4}
#    result = []
#    number_list_result = []
#    list_S = list(S)
#
#    for i in range(len(P)):
#        if "A" in list_S[P[i]:Q[i] + 1]:
#            number_list_result.append(1)
#        elif "C" in list_S[P[i]:Q[i] + 1]:
#            number_list_result.append(2)
#        elif "G" in list_S[P[i]:Q[i] + 1]:
#            number_list_result.append(3)
#        elif "T" in list_S[P[i]:Q[i] + 1]:
#            number_list_result.append(4)
#    return number_list_result
#
#solution(S,P,Q)

#
def solution(S, P, Q):
    n = len(S)
    a = [0] * (n+1)
    c = [0] * (n+1)
    g = [0] * (n+1)

    for i in range(1, n+1):
        print("I:", i)
        s = S[i-1]
        print('s:', s)
        a[i] = a[i-1]
        print("a[i]", a[i])
        print("a[i-1]", a[i-1])
        c[i] = c[i-1]
        print("c[i]", c[i])
        print("c[i-1]", c[i-1])
        g[i] = g[i-1]
        print("g[i]", g[i])
        print("g[i-1]", g[i-1])
        print(" ")
        if s == 'A':
            a[i] += 1
        elif s == 'C':
            c[i] += 1
        elif s == 'G':
            g[i] += 1
    print("a:", a)
    print("c:", c)
    print("g:", g)

    pqlen = len(P)
    results = [4] * pqlen

    for i in range(pqlen):
        p, q = P[i], Q[i]+1
        if a[q] - a[p] > 0:
            results[i] = 1
            continue
        elif c[q] - c[p] > 0:
            results[i] = 2
            continue
        elif g[q] - g[p] > 0:
            results[i] = 3
            continue

    return results

print(solution(S,P,Q))

