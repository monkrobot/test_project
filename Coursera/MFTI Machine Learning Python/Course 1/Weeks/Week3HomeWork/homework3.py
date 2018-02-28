##Exercise 1
#
#import math
#from scipy.optimize import minimize, rosen, rosen_der
#import matplotlib.pyplot as plt
#
#def func1(x):
#    f = math.sin(x / 5.) * math.exp(x / 10.) + 5 * math.exp(-x / 2.)
#    return f
#
#x0 = 2
#y0 = 30
#res = minimize(func1, x0, method='BFGS', tol=1e-6)
#print('for func1:', res.x)
#
#f = lambda x: math.sin(x / 5.) * math.exp(x / 10.) + 5 * math.exp(-x / 2.)
#res1 = minimize(f, y0, method='BFGS', tol=1e-6)
#print('for func1:', res1.x)
#
#z = [k for k in range(0, 40, 1)]
#k = [math.sin(x / 5.) * math.exp(x / 10.) + 5 * math.exp(-x / 2.) for x in z]
#print(k)
#plt.plot(z, k, color='green', linestyle='dashed', marker='o', markerfacecolor='blue', markersize=12)
#
#plt.show()

#Exercise2



