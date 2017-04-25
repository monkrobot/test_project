#This functions shows the max of zeros between '1' and '1'
def solution(N):
    binary_value = bin(N)[2:]
    print('binary_value:', binary_value)
    count_i = 0
    binary_gap = 0
    for i in binary_value[1:]:
        count_i += 1
        if i == '1':
            if binary_gap > count_i-1:
                count_i = 0
            else:
                binary_gap = count_i-1
                count_i = 0
        else:
            continue
    return binary_gap

print(solution(1041))