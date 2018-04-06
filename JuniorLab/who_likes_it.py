a = []
b = ['A']
c = ['A', 'B']
d = ['A', 'B', 'C']
e = ['A', 'B', 'C', 'D', 'E']

#def func(people):
#    len_p = len(people)
#    if len_p == 1:
#        return str(people[0]) + " likes this"
#    if len_p == 2:
#        return str(people[0]) + " and " + str(people[1]) + " like this"
#    if len_p == 3:
#        return str(people[0]) + ", " + str(people[1]) + " and " + str(people[2]) + " like this"
#    if len_p >= 4:
#        return str(people[0]) + ", " + str(people[1]) + " and " + str(len_p-2) + " others like this"
#    else:
#        return "no one likes this"

def func(people):
    len_p = len(people)
    if len_p == 0:
        return "no one likes this"
    else:
        return str(people[0]) + func(people[1:]) + "likes this"

print(func(b))
