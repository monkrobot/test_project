A = [4,2,2,5,1,5,8]
minimum_sum = float('inf')
minimum_P = float('inf')

for P in range(len(A)-1):
    for Q in range(P+1, len(A)):
        slice_avr = sum(A[P:Q+1])/(Q-P+1)
        print('slice_avr: ', slice_avr)
        if slice_avr < minimum_sum:
            minimum_sum = slice_avr
            print('minimum_sum ', minimum_sum)
            minimum_P = P
        elif slice_avr == minimum_sum:
            if P <= minimum_P:
                minimum_p = P
                print('minimum_P ', minimum_P)
            else:
                pass


print('Result sum: ', minimum_sum)
print('Result P: ', minimum_P)

#while A != []:
#    minimal = min(A)
#    index_minimal = A.index(minimal)
#    sum_slice = sum(A[index_minimal:index_minimal + 2]) / 2
#    if sum_slice < minimum_sum:
#        minimum_sum = sum_slice
#    print(index_minimal)
#    print(sum(A[index_minimal:index_minimal + 2]) / 2)
#    print(A[index_minimal - 1:index_minimal + 1])
#    print('minimum_sum', minimum_sum)
#    number = A.pop(A.index(minimal))