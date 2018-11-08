'''
Выведите таблицу размером n×n, заполненную числами от 1 до n2 по спирали, выходящей из левого верхнего угла
и закрученной по часовой стрелке, как показано в примере (здесь n=5):

1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
'''

num = int(input())
nums = [x for x in range(1, num**2+1)]

ans = [[0]*num]*num
answer = []
for raw in ans:
    answer.append(raw[:])

mat_num = 1
if num == 1:
    print(1)
else:
    for i in range(len(answer)):
        for j in range(i, len(answer)):
            if answer[i][j] == 0:
                answer[i][j] = mat_num
                mat_num += 1
                last_j = j
            else:
                break

        for k in range(i+1, len(answer)):
            if answer[k][last_j] == 0:
                answer[k][last_j] = mat_num
                mat_num += 1
                last_i = k
            else:
                break

        for m in range(last_j-1, -1, -1):
            if answer[last_i][m] == 0:
                answer[last_i][m] = mat_num
                mat_num += 1
                last_j = m
            else:
                break
        for n in range(last_i-1, 0, -1):
            if answer[n][last_j] == 0:
                answer[n][last_j] = mat_num
                mat_num += 1
                last_i = n
            else:
                break

    print(answer)
    for i in range(len(answer)):
        for j in range(len(answer[0])):
            if j != len(answer)-1:
                print(answer[i][j], end=" ")
            else:
                print(answer[i][j])









