##Exercise 1
##min: [4.13628869]
##function min: [25.88019339]
#
#import math
#from scipy.optimize import minimize
#import matplotlib.pyplot as plt
#
#def func1(x):
#    f = math.sin(x / 5.) * math.exp(x / 10.) + 5 * math.exp(-x / 2.)
#    return f
#
#x0 = 2
#y0 = 70
#res = minimize(func1, x0, method='BFGS', tol=1e-6)
#print('for func1:', res.x)

#f = lambda x: math.sin(x / 5.) * math.exp(x / 10.) + 5 * math.exp(-x / 2.)
#res1 = minimize(f, y0, method='BFGS', tol=1e-6)
#print('for func1:', res1.x)
#
#z = [k for k in range(10)]
#k = [func1(x) for x in z]
#print(k)
#plt.plot(z, k, color='green', linestyle='dashed', marker='o', markerfacecolor='blue', markersize=12)
#
#plt.show()

##Exercise2
##function min = x: array([88.712036])
#import math
#from scipy.optimize import differential_evolution
#
#def func1(x):
#    f = math.sin(x / 5.) * math.exp(x / 10.) + 5 * math.exp(-x / 2.)
#    return f
#
#bounds = [(1,100)]
#result = differential_evolution(func1, bounds)
#print(result)

##Exercise3
import math
from numpy import arange
import matplotlib.pyplot as plt
from scipy.optimize import minimize, differential_evolution

def func1(x):
    f = math.sin(x / 5.) * math.exp(x / 10.) + 5 * math.exp(-x / 2.)
    return f

def h_func(x):
    h = int(func1(x))
    return h

print('h_func(90):',h_func(90))

x = [k for k in arange(0, 30, 0.01)]
y = [h_func(x) for x in x]

x0 = 2
res = minimize(h_func, x0, method='BFGS', tol=1e-6)
print('res:', res.x)

bounds = [(1, 45)]
result = differential_evolution(h_func,bounds)
print('result:', result)
print('result.x:', result.x)

plt.plot(x,y)
plt.show()
