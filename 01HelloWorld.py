import math
import matplotlib.pyplot as plt
x = []
y = []
def func123(yo, xo, x1):
    x0 = 0
    y0 = 0
    error = 0
    deltax = abs(x1 - x0)
    deltay = abs(x1 * math.tan(yo/xo) - y0)
    deltaerr = deltay
    ys = y0

    for x_point in range(x0, x1):
        x.append(x_point)
        print('ys', x_point, ys)
        error = error + deltaerr
        if 2*error >= deltax:
            ys = ys-1
            error = error - deltax
        y.append(ys)

func123(4, 6, 7)
print('x', x)
fig = plt.figure()
plt.plot(x, y)
plt.show()