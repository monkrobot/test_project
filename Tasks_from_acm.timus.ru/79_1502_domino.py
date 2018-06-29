data = input('enter max number')
summ = 0
for i in range(1, data+1):
    for j in range(0, i+1):
        summ += i+j

print(summ)