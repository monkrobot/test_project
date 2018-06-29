import re

dictionary = ['na', 'ni', 'no', 'ki', 'ka', 'mu']
symbol = 'n'
count = 0

for i in range(0, len(dictionary)):
    if re.search('^' + str(symbol), dictionary[i]):
        print(dictionary[i])
        count += 1
if count == 0:
    print(-1)
else:
    print(count)


#for k in range(0, len(dictionary)):
#    print(re.search('^k', dictionary))