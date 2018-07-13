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

l = '2424'

if l.isdigit():
    print(True)