enter_data = '10 !!'
data_split = enter_data.split(' ')

i = int(data_split[0])
factorial = int(data_split[0])
if i <=0:
    print("error")
while i > 0:
    factorial *= (i - len(data_split[1]))
    i -= len(data_split[1])
    if i <= 0:
        break
    else:
        print('i: ', i)
        print('factorial', factorial)