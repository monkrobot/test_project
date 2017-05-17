A = [4,2,2,5,1,5,8]
minimum_sum = float('inf')


while A != []:
    minimal = min(A)
    index_minimal = A.index(minimal)
    sum_slice = sum(A[index_minimal:index_minimal + 2]) / 2
    if sum_slice < minimum_sum:
        minimum_sum = sum_slice
    print(index_minimal)
    print(sum(A[index_minimal:index_minimal + 2]) / 2)
    print(A[index_minimal - 1:index_minimal + 1])
    print('minimum_sum', minimum_sum)
    number = A.pop(A.index(minimal))