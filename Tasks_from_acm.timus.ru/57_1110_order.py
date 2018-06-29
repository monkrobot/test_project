n = 2
m = 4
y = 3
answer = []

for x in range(0, m):
    if x**n % m == y:
        answer.append(x)
    else:
        continue

if answer == []:
    print(-1)
else:
    for i in range(0, len(answer)):
        print(int(answer[i]))