##timer
#import time, sys, math
#timefunc = time.clock if sys.platform == "win32" else time.time
#
#def timer(func, *pargs, _reps=1000, **kargs):
#    start = timefunc()
#    for i in range(_reps):
#        ret = func(*pargs, **kargs)
#    elapsed = timefunc() - start
#    return elapsed, ret
#
#def best(func, *pargs, _reps = 100, **kwargs):
#    best = 2**32
#    for i in range(_reps):
#        (time, ret) = timer(func, *pargs, _reps=1, **kwargs)
#        if time < best:
#            best = time
#    return best, ret
#
#for i in (lambda x: math.sqrt(x), lambda x: x**0.5, lambda x: pow(x, 0.5)):
#    print('time:', timer(i, 25))
#    print('best:', best(i, 25))

#print(timer((lambda x: '%s' % x), ('hello')))
#print(timer((lambda x: '{0}'.format(x)), ('buy')))
#
#print('-'*15)
#print(best((lambda x: '%s' % x), ('hello'), _reps = 1000))
#print(best((lambda x: '{0}'.format(x)), ('buy'), _reps = 1000))


# def decor(func):
#     def wrapper(*args, **kwargs):
#         print('wrapper')
#         return func(*args, **kwargs)
#     return wrapper
#
# @decor
# def test(text):
#     return (f'hello, {text}')
#
# @decor
# def test1(numb):
#     print(f'one plus {numb} is {1 + numb}')
#
# print(test('Ol'))
# test1(12)
#
# help(test1)

a = 7
b = 20
c = 4
queue = [1,5,3,45,2]
letters = [a,b,c]
for j in range(len(letters)):
    for k in range(j, len(letters)):
        if

for i in queue:

    if a<b and a<c:
        a += i
    elif b<a and b<c:
        b += i
    else:
        c += i

print(a)
print(b)
print(c)
print("max:", max(a,b,c))







# def queue_time(customers, n):
#     # if customers == []:
#     #     customers = [0]
#     # print(min(customers[:n]))
#
#     answer = []
#     for i in range(n):
#         answer.append([customers[i]])
#     for j in range(customers[(n - 1):]):
#         min(answer).append(j)
#
#         # customer = (x for x in customers[(n-1):])
#
# queue_time([1,2,3,4,5], 1)
# queue_time([1,2,3,4,5], 100)




