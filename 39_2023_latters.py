import math
#first = ['a', 'p', 'o', 'r']
#second = ['b', 'm', 's']
#third = ['d', 'g', 'j', 'k', 't', 'w']

letters = ['b', 'd', 'p', 'a']
#letter2 = 'd'
#letter3 = 'p'
#letter4 = 'm'
old_step = 1
steps = 0

latter = {1: ['a', 'p'], 2: ['b', 'm', 's'], 3: ['d', 'g', 'j', 'k', 't', 'w']}
lat_val = latter.items()


for i in range(0, len(letters)):
    for j in range(0, len(lat_val)):
        if letters[i] in lat_val[j][1]:
            steps += math.fabs(old_step - int(lat_val[j][0]))
            old_step = int(lat_val[j][0])
            print("step " + str(i) + ": " + str(steps))
            print(old_step)

        else:
            continue
print("steps " + str(steps))

#['a', 'p', 'o', 'r']