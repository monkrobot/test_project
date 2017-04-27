#Find min positive number, which isn't included in list A
#problems with work speed 77%

def solution(A):
    if A == [1]:
        return 2
    B = sorted(A)
    if B[0] > 1 or B[-1] < 1:
        return 1
    C = [i for i in B if i > 0]
    print(C)
    help_number = C[0]
    if C[0] != 1:
        return 1
    else:
        for j in range(len(C)-1):
            print('C[j]', C[j+1])
            if C[j+1] == help_number:
                continue
            elif C[j+1] == help_number + 1:
                help_number = C[j+1]
                print('help_number',help_number)
            else:
                return help_number+1


A = [-5,0,1,2,30]
print(solution(A))