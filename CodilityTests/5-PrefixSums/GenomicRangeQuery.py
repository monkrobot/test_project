#25%
S = "CAGCCTA"
P = [0,5,2]
Q = [4,5,5]

def solution(S, P, Q):
    """S - string DNA information, P and Q - arrays with numbers"""
    dict_DNA = {'A': 1, 'C': 2, 'G': 3, 'T':4}
    result = []
    number_list_S = []
    for dna in list(S):
        if dna in dict_DNA:
            number_list_S.append(dict_DNA[dna])

    for i in range(len(P)):
        if P[i] != Q[i]:
            slice_result = number_list_S[P[i]:Q[i]]
            print('slice_result', slice_result)
            result.append(min(slice_result))
        else:
            slice_result = number_list_S[P[i]]
            print('slice_result', slice_result)
            result.append(slice_result)
        print(result)

solution(S,P,Q)